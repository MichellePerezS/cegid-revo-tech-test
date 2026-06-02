#EXERCISE 2 COLLECTIONS 2

TARGET_TYPES = ["Wallet","Lamp"]

def is_target_product(product):
    return product.get("product_type") in TARGET_TYPES

def sum_variant_prices(product):
    variants = product.get("variants",[])
    prices = map(lambda v: v.get('price',0),variants)
    return sum(prices)

def calculate_total_cost(product_list):
    filter_products=filter(is_target_product,product_list)
    total_product = map(sum_variant_prices,filter_products)
    return sum(total_product)

def run_test():
    mock_products =[
    {
	    	"title": "Small Rubber Wallet",
	    	"product_type": "Wallet",
	    	"variants": [
	      		{ "title": "Blue", "price": 29.33 },
	      		{ "title": "Turquoise", "price": 18.50 }
	    	]
		}, {
		
			"title": "Sleek Cotton Shoes",
			"product_type": "Shoes",
			"variants": [
	  			{ "title": "Sky Blue", "price": 20.00 }
			]

	 	}
        ]
    result = calculate_total_cost(mock_products)

    assert round(result,2)==47.83
    print("TEst successfully passed")

if __name__ == "__main__":
    run_test()