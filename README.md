<h1>Django Recipe Website</h1>

<h2>Info</h2>
<p>This project was developed using the Django MVT architecture, with function base views.py and modules such as the Django automatic email module, image compression, pagination, relational databases, Bootstrap, data search functionality, and password modification functionality. It is deployed on Fly.io using AWS S3 and RD database.</p>

<h2>Install</h2>
To install relative module

1. git clone https://github.com/SiaoChi/recipe/
2. pip install -ur requirements.txt (os)
3. change your database information
4. executive 
```
python manage.py makemigrations
python manage.py migrate
```
5. create superuser
```
python manage.py createsuperuser
```

6. static
```
python manage.py collectstatic --noinput
```
7. run server
```
python manage.py
```

<h2>Usage</h2>

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

