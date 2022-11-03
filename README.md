# [Tree of Thought](https://www.treeofthought.com/) Back end API

## Usage
### `flask run` 
launch the application.

### `flask test`
run unit tests

### `flask shell`
launch interactive shell

### `flask lint`
run linting

## TODO
* Better handling of images...
  * Move them from seed files to static during DB seed
  * Make the prefix which must be added to image urls a configurable variable
* Paginate route for accessing blog list
* Document routes
* Secure CORS implementation so API only talks to front end
* DB Model and endpoints for "top tens" 