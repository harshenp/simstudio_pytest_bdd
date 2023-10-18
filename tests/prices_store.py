from selenium.webdriver.common.by import By

price_zyngBeanz = []
price_others =[]

def prices(table):
    print("* Table 6 - Market Report *")
    row = table.find_element(By.XPATH, "//tr[contains(., 'Price')]")
    cells = row.find_elements(By.TAG_NAME, 'td')
    for i, cell in enumerate(cells):
        if i == 1:
            price_zyngBeanz.append(cell.text)
        if i > 1 :
            price_others.append(cell.text)
    print(price_zyngBeanz)
    print(price_others)