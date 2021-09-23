from jinja2 import Environment, FileSystemLoader, select_autoescape
import sys, os, json

def main():
    vars_file = sys.argv[1]
    pwd = os.getcwd()
    env = Environment(loader=FileSystemLoader("templates/"), autoescape=select_autoescape)
    templ = env.get_template("base_template.html")
    vars = {}
    with open(vars_file) as v:
        vars = json.load(v)
    templ.stream(vars).dump("development.html")




if __name__ == '__main__':
    main()