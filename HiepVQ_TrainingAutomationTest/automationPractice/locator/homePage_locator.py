class HomePage_locator:
    signInButton_linkText = 'Sign in'
    newsletter_id = 'newsletter-input'
    submitNewsletter_xpath = "//button[@name='submitNewsletter']"
    allertSuccess_xpath = '//p[@class="alert alert-success"]'
    contactUs_linkText = 'Contact us'
    search_id = 'search_query_top'
    search_xpath = '//*[@id="search_query_top"]'
    all_suggest_keywords_xpath = "//div[@class='ac_results']//li[starts-with(@class,'ac_')]"
    searchButton_xpath = '//button[@name="submit_search"]'
    allProducts_xpath = '//*[@id="homefeatured"]/li'
    addToCart_xpath = '//span[contains(text(),"Add to cart")]'
    addToCart_link_text = 'Add to cart'
    continueShopping_xpath = '//span[@title="Continue shopping"]'
    proceedToCheckout_xpath = '//a[@title="Proceed to checkout"]'
    price_xpath = '//ul[@id="blockbestsellers"]//div[@class="left-block"]//span[@itemprop="price"]'
    allProductsPricePercentReduction = '//ul[@id="blockbestsellers"]//div[@class="left-block"]//span[@class="price-percent-reduction"]'
    productImage_xpath = "//ul[@id='blockbestsellers']//a[@class='product_img_link']"

