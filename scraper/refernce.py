

    # def search_items(self):
    #     j = 0
    #     all_items_info = []
    #     constant_window=self.current_window_handle
    #     for i in link_list:
    #         search_bar = self.find_element(By.ID, "twotabsearchtextbox")
    #         search_bar.send_keys("asin" + " " + i)
    #         time.sleep(2)
    #         search_bar.send_keys(keys.ENTER)
    #         time.sleep(0.3)
    #         box = self.find_element(By.CSS_SELECTOR, "div[class='a-section a-spacing-small puis-padding-left-small puis-padding-right-small'] a[class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']")
    #         box.click()
    #         time.sleep(10)

    #         # Get the original window handle
    #         # original_window_handle = self.current_window_handle
    #         # # Switch to the new window
    #         # all_window_handles = self.window_handles
    #         # for handle in all_window_handles:
    #         #     if handle != original_window_handle:
    #         #         self.switch_to.window(handle)
    #         #         break

    #         try:
    #             # Perform actions in the new window
    #             price_element = WebDriverWait(self, 10).until(
    #                 ec.visibility_of_element_located((By.CLASS_NAME, 'a-price-whole'))
    #             )
    #             price = int(price_element.text.replace(",", ""))

    #         except Exception as e:
    #             price = "None"

    #         merchant_info_div = WebDriverWait(self, 10).until(
    #             ec.visibility_of_element_located((By.ID, 'merchant-info'))
    #         )
    #         merchant_info = merchant_info_div.find_element(By.TAG_NAME, 'a').text

    #         if merchant_info != "ETrade Online":
    #             offer_divs = self.find_elements(By.CSS_SELECTOR, 'div.a-box.mbc-offer-row.pa_mbc_on_amazon_offer')
    #             for offer_div in offer_divs:
    #                 merchant_name_element = offer_div.find_element(By.CSS_SELECTOR, 'span.mbcMerchantName')
    #                 merchant_name = merchant_name_element.text.strip()

    #                 if merchant_name == "ETrade Online":
    #                     price_element_ET = offer_div.find_element(By.CSS_SELECTOR, 'span.a-size-medium.a-color-price')
    #                     price_ET = price_element_ET.text.strip()
    #                     break  # Stop iterating through the offer divs once we find
    #                 else:
    #                     continue
    #         else:
    #             price_ET = None

    #         Et_live = "yes" if merchant_info == "ETrade Online" else "no"
    #         Et_mop = "yes" if price == price_list[j] else "None"
    #         bb_seller_p = None if price == price_list[j] else price
    #         bb_seller_name = merchant_info
    #         et_cost = price_ET
    #         j += 1
            

    #         # Append the item info to the list
    #         all_items_info.append([Et_live, Et_mop, bb_seller_p, bb_seller_name, et_cost])

    #         # Switch back to the original window
    #         # self.switch_to.window(constant_window)
    #         time.sleep(0.1)
    #         search_bar = self.find_element(By.ID, "twotabsearchtextbox").clear()
    #         time.sleep(0.5)
    #         print(all_items_info)

    #         if j == 10:
    #             break

    #     return all_items_info