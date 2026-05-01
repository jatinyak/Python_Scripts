from playwright.sync_api import sync_playwright

BASE_URL = "https://help.sap.com/doc/abapdocu_cp_index_htm/CLOUD/en-US/"
START_PAGE = "ABENABAP_REFERENCE.html"
OUTPUT_FILE = "SAP_Cloud_Reference_Complete.txt"

def crawl_sap_docs(start_page, output_filename):
    visited_urls = set()
    # This acts as our "To-Do" list of pages to click
    urls_to_visit = [start_page]
    
    with sync_playwright() as p:
        # Keep headless=False so you can watch it work
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Clear the file and write a header
        with open(output_filename, "w", encoding="utf-8") as f:
            f.write("SAP ABAP CLOUD REFERENCE\n\n")

        while urls_to_visit:
            # Get the next page from the to-do list
            current_page = urls_to_visit.pop(0)
            
            # Clean the URL (remove # anchor tags so we don't visit the same page twice)
            current_page = current_page.split('#')[0]
            
            if current_page in visited_urls:
                continue
                
            visited_urls.add(current_page)
            full_url = BASE_URL + current_page
            
            print(f"[{len(visited_urls)} pages saved] Scraping: {current_page} ... ({len(urls_to_visit)} left in queue)")
            
            try:
                # 1. Go to the page and wait for the text to appear
                page.goto(full_url, wait_until="networkidle")
                page.wait_for_timeout(1000) # Give it 1 second to settle
                
                # 2. Extract the text
                # We try to grab just the actual reading content ('div.item' or 'main') to avoid copying the sidebars
                content_locator = page.locator("div.item").first
                if content_locator.is_visible():
                    visible_text = content_locator.inner_text()
                else:
                    # Fallback if the layout changes
                    visible_text = page.locator("body").inner_text()

                # Save it to the file
                with open(output_filename, "a", encoding="utf-8") as f:
                    f.write(f"\n\n{'='*80}\n")
                    f.write(f"SOURCE URL: {full_url}\n")
                    f.write(f"{'='*80}\n\n")
                    f.write(visible_text)
                
                # 3. Find all the new links on this page to add to our To-Do list
                # This grabs every 'href' link visible on the page
                hrefs = page.eval_on_selector_all("a[href]", "elements => elements.map(e => e.getAttribute('href'))")
                
                for href in hrefs:
                    href = href.split('#')[0]
                    lower_href = href.lower()
                    
                    # We only want to add links that belong to the ABAP documentation (start with 'aben' or 'abap')
                    if (lower_href.startswith("aben") or lower_href.startswith("abap")) and lower_href.endswith(".html"):
                        if href not in visited_urls and href not in urls_to_visit:
                            urls_to_visit.append(href)
                            
            except Exception as e:
                print(f"Skipped {current_page} due to an error: {e}")
        
        browser.close()
        print("\nFinished crawling! All pages have been saved to the text file.")

# Run the crawler
crawl_sap_docs(START_PAGE, OUTPUT_FILE)