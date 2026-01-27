# How to draw bar chart in Python
```python
import matplotlib.pyplot as plt

products = ['A', 'B', 'C', 'D']
sales = [40, 70, 55 90]

plt.bar(products, sales)
plt.xlabel('Products')
plt.ylabel('Sales')
plt.title('Sales by Products')

plt.show()
```
