# Django Recipe Website
![pic](https://github.com/SiaoChi/recipe/assets/98171354/131366ba-c0ca-4df9-8755-41648670ca90)

## Info
This project was developed using the Django MVT architecture, with function base views.py and modules such as the Django automatic email module, image compression, pagination, relational databases, Bootstrap, data search functionality, and password modification functionality. It is deployed on Fly.io using AWS S3 and RD database.

## Install
To install relative module

1. git clone https://github.com/SiaoChi/recipe/
2. pip install -ur requirements.txt (os)
3. change your database information
4. executive 

```
python manage.py makemigrations
python manage.py migrate
```

### create superuser
```
python manage.py createsuperuser
```

### static
```
python manage.py collectstatic --noinput
```
### run server
```
python manage.py runserver
```

### Feature

1. Browse recipes:
   - On the home page, you can see all the recipes.
   - You can filter the recipes by the search bar.
   - You can also search for recipes by ingredients.

2. Create a recipe:
   - To create a recipe, you must be logged in as a user.
   - Click on "Create Recipe" button in the navigation bar.
   - Fill in the recipe details, including the ingredients and instructions.
   - Click on "Save" to save the recipe.

3. Edit/Delete a recipe:
   - To edit or delete a recipe, you must be the owner of the recipe.
   - Click on the recipe to view it.
   - Click on the "Edit" button to edit the recipe.
   - Click on the "Delete" button to delete the recipe.


### website UI
首頁總覽<br>
![pic](https://github.com/SiaoChi/recipe/assets/98171354/131366ba-c0ca-4df9-8755-41648670ca90)

食譜畫面<br>
![2](https://github.com/SiaoChi/recipe/assets/98171354/fa16f0e9-fd58-4ac8-b494-ee3e6e0233e2)

建立食譜畫面<br>
![4](https://github.com/SiaoChi/recipe/assets/98171354/6cf6114b-8e8f-4a8e-9f03-c10bcfc5a943)
![5](https://github.com/SiaoChi/recipe/assets/98171354/feb0aef9-0d22-4be4-9a05-43f3513fb84b)


