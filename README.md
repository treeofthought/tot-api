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

## Database management...
`scratch/seed_heroku.txt` has commands for SSHing to the heroku dyno and populating the database based on the `posts/` folder.

You'll need to manually add images to `app/static/`

## TODO
* Better handling of images...
  * Move them from seed files to static during DB seed
* Paginate route for accessing blog list
* Document routes
* Secure CORS implementation so API only talks to front end
* Decouple the content source (eg, `posts/` folder) from the application
