from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = { "my_list": [ 
			{
                "restaurant_name":"McDonald's",
                "food_type":"Fast food",
            },
            {
                "restaurant_name":"Pizza Hut",
                "food_type":"Pizza",
            },
            {
                "restaurant_name":"Sbarro",
                "food_type":"Italian",
            },
			]

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
		"my_object": {
		"restaurant_name":"Hardees",
		"food_type":"Fast food",
				
		}
    }
    return render(request, 'detail.html', context)
