# Coffee statistics chart

Creates bar chart from the export file of the coffee machine.

## Requirements

* Python 3.X
* Numpy
* Pandas
* Matplotlib

## Usage

### Run

```
python coffee.py /.../data.cs
```

### New kind of coffee

Add new entry to the config.json. It should follow this pattern:
```
"_name_in_coffee_machine_": {
	"language": "_chosen_programming_language_",
	"color": "#XXXXXX",
	"altNames": []  #list of alternative names, usefull if coffee type is renamed
	}
```
