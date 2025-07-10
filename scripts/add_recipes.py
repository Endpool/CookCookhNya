import json
import urllib.request
import urllib.error
import sys
from typing import Callable

def load_recipes(json_file_path: str):
  try:
    with open(json_file_path, 'r', encoding='utf-8') as file:
      return json.load(file)
  except FileNotFoundError:
    print(f"Error: File {json_file_path} not found")
    sys.exit(1)
  except json.JSONDecodeError as e:
    print(f"Error: Invalid JSON format in {json_file_path} - {str(e)}")
    sys.exit(1)

def create_recipe(endpoint_url: str, recipe):
  headers = {
    'Content-Type': 'application/json',
  }
  recipe_data = {
    'name': recipe['name'],
    'sourceLink': recipe['url'],
    'ingredients': recipe['ingredient_ids'],
  }
  data = json.dumps(recipe_data).encode('utf-8')

  try:
    req = urllib.request.Request(endpoint_url, data=data, headers=headers, method='POST')
    with urllib.request.urlopen(req) as response:
      if response.getcode() == 200:
        response_data = json.loads(response.read().decode('utf-8'))
        return f"Successfully created recipe '{recipe['name']}': {response_data}"
      else:
        return f"Failed to create recipe '{recipe['name']}': {response.getcode()} - {response.read().decode('utf-8')}"
  except urllib.error.HTTPError as e:
    return f"Error creating recipe '{recipe['name']}': HTTP {e.code} - {e.read().decode('utf-8')}"
  except urllib.error.URLError as e:
    return f"Error creating recipe '{recipe['name']}': {str(e)}"
  except Exception as e:
    return f"Unexpected error creating recipe '{recipe['name']}': {str(e)}"

def load_ingredient_id(all_ingredients: list[tuple[int, str]]) -> Callable[[str], int | str]:
  def f(ingredient: str):
    a = [id for (id, ingr) in all_ingredients if ingr == ingredient]
    return a[0] if len(a) >= 1 else f'Could not find {ingredient}'
  return f

def get_ingredients(endpoint_url: str) -> str | list[tuple[int, str]]:
  try:
    req = urllib.request.Request(endpoint_url, method='GET')
    with urllib.request.urlopen(req) as response:
      if response.getcode() == 200:
        return [(ingr['id'], ingr['name']) for ingr in json.loads(response.read().decode('utf-8'))]
      else:
        return f"Failed to create fetch all ingredients': {response.getcode()} - {response.read().decode('utf-8')}"
  except urllib.error.HTTPError as e:
    return f"Error fetching all ingredients': HTTP {e.code} - {e.read().decode('utf-8')}"
  except urllib.error.URLError as e:
    return f"Error fetching all ingredients': {str(e)}"
  except Exception as e:
    return f"Unexpected error fetching all ingredients': {str(e)}"

def get_first_string_or_ints(items: list[int | str]) -> str | list[int]:
    return next((item for item in items if isinstance(item, str)), [item for item in items if isinstance(item, int)])

def load_ingredient_ids(all_ingredients: list[tuple[int, str]], ingredients) -> list[int] | str:
  if isinstance(all_ingredients, str):
    return all_ingredients

  loaded = get_first_string_or_ints(
    list(
      map(
        load_ingredient_id(all_ingredients),
        map(lambda s: s.lower(), ingredients)
      )
  ))
  if isinstance(loaded, str):
    return loaded

  return loaded

def main():
  if len(sys.argv) != 2:
    print("Usage: python add_recipes.py <recipes_json_file>")
    sys.exit(1)

  json_file_path = sys.argv[1]
  endpoint_url = "http://localhost:8080/recipes"
  get_ingredients_url = "http://localhost:8080/ingredients"

  recipes = load_recipes(json_file_path)

  all_ingredients = get_ingredients(get_ingredients_url)
  if isinstance(all_ingredients, str):
    print(all_ingredients)
    return

  for recipe in recipes:
    ingredient_ids = load_ingredient_ids(all_ingredients, recipe['ingredients'])
    if isinstance(ingredient_ids, str):
      print(ingredient_ids)
      continue

    recipe['ingredient_ids'] = ingredient_ids
    result = create_recipe(endpoint_url, recipe)
    print(result)

if __name__ == "__main__":
  main()
