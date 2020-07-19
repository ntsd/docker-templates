# Docker Templates

This is my templates for make things easier to setup

## Useful scripts

### Replace shell command in .env.example to .env

``` Shell
eval "echo \"$(cat .env.example)\"" > .env
```
