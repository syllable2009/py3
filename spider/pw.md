# 请求回来的html可以使用lxml解析以外，PW也有自己推荐的内置定位器

# playwright定位器

# 定位器代表一种随时查找页面上元素的方法，可以使用page.locator()方法创建定位器。

# filter, locator, and_, or_

# filter过滤

has_text or has_not_text过滤
page.get_by_role("listitem").filter(has_text="Product 2") 定位到第二个li
has or not_has过滤
page.get_by_role("listitem").filter(has=page.get_by_role("heading", name="Product 2")
) 定位到第二个li

# locator

只会匹配visible的button
page.locator("button").locator("visible=true")

# 计数断言
expect(page.get_by_role("listitem")).to_have_count(3)
expect(page.get_by_role("listitem")).to_have_text(["apple", "banana", "orange"])
expect(page.get_by_text("Name")).to_be_visible(timeout=10_000)

# 获取第 n 个 
banana = page.get_by_role("listitem").nth(1)
locator.first
locator.last
locator.all()

# 选择后截图
page.get_by_role("listitem").nth(1).screenshot(path="screenshot.png")

# 迭代
for row in page.get_by_role("listitem").all():
    print(row.text_content())
rows = page.get_by_role("listitem")
count = rows.count()
for i in range(count):
    print(rows.nth(i).text_content())

# 同时匹配两个定位器

page.get_by_role("heading").and_(page.get_by_text("product 1"))

# 满足两个定位器之中一个, 如果两个均匹配到，但不是同一个元素会报 multiple elements

page.get_by_role("heading").or_(page.get_by_text("product 1"))

# 推荐的内置定位器

# role通过显式和隐式可访问性属性进行定位。

page.get_by_role("button", name="Sign in").click()   <button>Sign in</button>
page.get_by_role("button", name=re.compile("submit", re.IGNORECASE)).click()
常见的role的值有 link, button, heading, checkbox, list, listitem, textbox, form, table, row, cell等，
具体其他role, 可查看https://www.w3.org/TR/html-aria/#docconformance

# placeholder通过占位符定位输入。

page.get_by_placeholder("Please input
password")  <input type="password" placeholder="Please input  password" />

# label通过关联标签的文本定位表单控件

page.get_by_label("Password").fill("string")   <label>Password <input type="password" /></label>

# alt_text通过替代文本来定位元素（通常是图像）。

page.get_by_alt_text("playwright
logo") <img alt="playwright logo" src="/img/playwright-logo.svg" width="100" />

# title通过元素的标题属性来定位元素。

page.get_by_title("status") <li title="status" role="menuitem" > status</li>

# text通过元素包含的文本来定位该元素

page.get_by_text("Password") <span>Password </span>
page.get_by_text("string") 模糊匹配的,不区分大小写
page.get_by_text("string", exact=True) 精确匹配, 区分大小写
page.get_by_text(re.compile("submit", re.IGNORECASE)) 正则匹配

# test_id根据元素的属性定位元素data-testid（可以配置其他属性）。

page.get_by_test_id("directions") <button data-testid="directions">Itinéraire</button>
可以通过playwright.selectors.set_test_id_attribute("data-pw") 设置获取的属性是data-pw,
这样设置后page.get_by_test_id("directions")表示获取的是data-pw属性是directtions的元素。

# xpath
page.locator("xpath=//button").click()
page.locator("//*[@id="tsf"]")

# css #id .class
page.locator("css=button").click()
page.locator(".css_name")

# 查找一个元素的父元素

page.get_by_text("product 1").locator("..") 定位到文本是product 1的元素的父元素

# iframe定位

如果要定位iframe中的元素， 可以先page.frame_locator("my-frame")定位到iframe，再定位到具体的元素