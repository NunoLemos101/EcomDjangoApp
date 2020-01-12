var all_products = document.getElementById('myUL');
var products = all_products.getElementsByTagName('ulx');

for (z = 0 ; z < products.length ; z++) {
    var pro  = products[z]
    pro = pro.outerHTML
    pro = pro.slice(9)
    var cut_by = pro.indexOf('>')
    pro = pro.slice(0 , cut_by - 1)
    pro = pro + 'title'
    pro_title = document.getElementById(pro)
    text_needed = pro_title.innerHTML
    if (text_needed.length >= 20) {
      text_needed = text_needed.slice(0 , 20)
      document.getElementById(pro).innerHTML = text_needed + '...'
    } else {
        continue
    }
  }