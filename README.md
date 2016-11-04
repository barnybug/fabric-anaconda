# Package for working with anaconda environments in Fabric

Usage:

```python
import fabriconda

def setup():
    fabriconda.install()

def deploy():
    put('environment.yml', '/path/to/environment.yml')
    fabriconda.create_env('/path/to/environment.yml', 'name')
    with fabriconda.env('name'):
    	pass # do stuff in the environment
```
