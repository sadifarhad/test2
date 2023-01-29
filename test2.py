amazon = AmazonApi(KEY, SECRET, TAG, COUNTRY)
product_content = ''

search_result = amazon.search_items(keywords=keyword)
for item in search_result.items:
    title = item.item_info.title.display_value
    wp_title = wp_heading_two(title)
    product_image_url = item.images.primary.large.url
    wp_image = wp_image_url(product_image_url,title)
    product_info = item.item_info.features.display_values
    wp_list = list_html(product_info)
    product_content = product_content + f'{wp_title}{wp_image}{wp_list}'
    
    2