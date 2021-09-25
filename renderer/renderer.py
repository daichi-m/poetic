from jinja2 import Environment, FileSystemLoader, select_autoescape
import sys, os, json

def human_readable_size(size: float, decimal_places: int=2) -> str:
    for unit in ['B','KiB','MiB','GiB','TiB']:
        if size < 1024.0:
            break
        size /= 1024.0
    return f"{size:.{decimal_places}f}{unit}"

def pandas_to_icon(pd_type: str) -> str:
    tp = pd_type.lower()
    if tp == "object":
        return "text_fields"
    elif tp == "int64" or tp == "float64" or tp == "numeric":
        return "looks_one"
    elif tp == "bool":
        return "toggle_off"
    elif tp == "datetime64" or tp == "timedelta":
        return "timer"
    elif tp == "categorical":
        return "category"
    else:
        return "help_outline"




def main():
#     vars_file = sys.argv[1]
    pwd = os.getcwd()
    env = Environment(loader=FileSystemLoader("templates/"), autoescape=select_autoescape)
    env.filters['byte_converter'] = human_readable_size
    env.filters['type_icon'] = pandas_to_icon
    templ = env.get_template("result.html.jinja")
    vars = {}
    vars_full = {}
    with open('iris_prof.json') as v:
        vars = json.load(v)
    with open('full_dataframe.json') as v2:
        vars_full = json.load(v2)
    vars.update(vars_full)
        
    templ.stream(vars).dump("development.html")

if __name__ == '__main__':
    main()