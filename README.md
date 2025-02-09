<!-- omit in toc -->
# Symbolic Regression using Genetic Programming
![Python](https://img.shields.io/badge/python-3.9-blue)
![License: MIT](https://img.shields.io/badge/license-MIT-green)
![Contributors](https://img.shields.io/badge/Contributors-4-brightgreen)
![Jupyter Notebook](https://img.shields.io/badge/notebook-Jupyter-orange)

## Project Collaboration
This project was developed in collaboration with my colleagues, whose GitHub names are listed in the Contributors section below. The full commit history, including contributions from all team members, can be found in the original repository of the [project](https://github.com/FerraiuoloP/CI2024_Project). Here, it is possible to track the entire development process and the evolution of our work.

## Description
This repository contains an implementation of a Symbolic Regression algorithm, using a tree-based **Genetic Programming** (GP) evolutionary technique. The algorithm evolves mathematical expressions in order to find the model that best fits a given set of data in the form $(X, y)$. By leveraging *selection*, according to a fitness measure, *mutation* and *crossover*, the SR algorithm generates mathematical formulas that are able to capture the complex patterns present in the input data.

## Key Features
- **Island Model Genetic Algorithm**
  - The population is divided into a certain number of **subpopulations** (a.k.a. *islands*) which evolve separately and can occasionaly exchange individuals (a.k.a *migration*) in order to avoid local optima and rapid convergence;
  - The migration happens in a probablistic way. At every iteration a random individual can be selected to migrate from an island to another one;
  - At each migration event, according to a migration rate parameter, one or more individuals migrate from the source island to another random island, as a way to ensure equal chance of genetic mixing across islands.
- **Tree-Based Representation**
  - The evolutionary algorithm iteratively evolves a population of mathematical formulas, represented as full and grow trees;
  - Internal nodes are randomly chosen from function set (arithmetic, trigonometric, logarithmic and exponential operators), while leaves are randomly chosen from terminal set (constants and variables);
  - Each tree contains at least one instance of each variable of the problem dataset;
  - Each tree must be consistent with the core principles of the mathematical system (*e.g.* no divisions by 0).
- **Elitism**
  - To preserve high-quality solutions, the best individuals (a.k.a. *elites*) are directly inserted into the next generation, without being subjected to any change.
- **Parents Selection**
  - Different parents selection strategies are implemented. Fitness-proportional, rank based and tournament selection. If not specified, the default rank-based strategy is used.
- **Mutation and Crossover**
  - Various mutation mechanisms are implemented. Replaced a subtree with a new one (`mutate_subtree`) or modify a single node (`mutate_single_node`) in the selected parent tree;
  - Combine two different trees for generating new offsprings. This allows the algorithm to explore new regions in the search space, encouraging exploration instead of exploitation.
- **Takeover Detection**
  - It is possible that a particularly suitable individual, with an important competitive advantage, dominates the population. Its offspring spread rapidly in the population and genetic diversity decreases. To address this issue, the population is trimmed by keeping alive only unique individuals and re-generating the remaining ones;
  - In the proposed algorithm, takeover occurs when 50% of the population exhibits the same fitness.  

## How it works
- **Initialization**
  - A population of individuals (*trees*) is initialized on each island. Depending on the value assigned to the variable `grow_full_ratio`, each island's population is initialized with a number of full trees and grow trees. Although the literature often suggests a grow full ratio of 0.50, the proposed solution adopts a ratio of 0.95. This approach allows for more diverse and flexible initial solutions, leading to better exploration of the search space and avoiding a bloating phenomenon, tipycal of the generation of large trees;
  - In each of the `ISLAND_NUM` islands, there are `ISLAND_POPULATION` individuals.
- **Selection**
  - Parents are selected based on their fitness (in which measure the mathematical formula represented by the tree fits well the data provided as input), using various strategies (*e.g.* rank-based selection).
- **Reproduction**
  - Offsprings are generated through mutation and crossover genetic operators (0.65/0.35 ratio).
- **Evolution**
  - Over the course of generations, populations on the islands evolve and only the best performing trees survive.
- **Convergence**
  - The evolutionary process continues for a certain number of generations (`MAX_GENERATIONS`).

## Project Structure
The project is organized as follows:
- `data/`
  - A folder that contains eight different input problems (*npz* files). Each problem is represented by a dataset that can be used to train and test the model.
- `src/sym_reg.ipynb`
  - The Jupyter notebook through which it is possible to experiment with Symbolic Regression using Genetic Programming. Thank to parent selection, mutation and crossover genetic operators, it is possible to find a mathematical formula that well fit the given dataset.
  ```python
  x[0] + np.sin(x[1]) / 5   # a simple mathematical formula for problem 0
  ```
- `src/tree.py`
  - The .py file that contains the **Tree** class, the main component of the project. This class provides methods for generating grow and full trees, methods for computing the fitness and methods for mutation and crossover.
- `src/pyproject.toml`
  - The configuration file containing dependencies and metadata for the project. *Poetry* is used for package management.
- `s325676.py`
  - The .py file that contains the formulas for the eight input problems in `data/`.

## Results

### Important Notes 
- **Variables Inclusion**: Each formula contains at least one instance of each variable;
- **Formula Simplification**: To enhance readability, all possible calculations are performed (this justifies the presence of constants outside the predefined range in the formula) and some NumPy operators, i.e. `np.add`, `np.subtract`, `np.multiply`, `np.divide`, have been replaced with the corresponding basic operators (+, -, *, /);
- **Formula Complexity**: A balanced approach between formula complexity (in depth) and MSE has been prioritized;
- **Hyperparameter Tuning**: Different hyperparameters have been used during different runs.

### Problem 1

**MSE**: 7.125940794232773e-34

```python
np.sin(x[0])
```

### Problem 2

**MSE**: 6767157331999.958

A high MSE value that indicates the formula does not accurately represent the relationship between the input and output values. This suggests that the existing relationship between the variables is highly complex, and the algorithm struggles to uncover it. It is worth noting that by adopting a higher number of generations, it would have been possible to achieve lower MSE values, reaching precision up to 12 decimal places, instead of the current 13. However, a particularly high value that would be obtained with a high computational cost, with a runtime exceeding two hours.

```python
(((((x[1] * 1.0133379750665732) * -19.919416233677293) + ((-9.790571207340218 * x[2]) + (-9.735723057413209 * x[2]))) * ((1711.0001133355208 * np.cosh(x[0])) + -40620.92739861885)) + ((-140.73135021910855 - ((x[2] * x[1]) * -10.82318841194864)) * ((36.04153204685458 / (1.0133379750665732 / x[0])) * -216.83639344361913)))
```

### Problem 3

**MSE**: 9.059643246177774e-05

```python
np.arctan(np.arctan(1.9423158330970622) + 8.311556888397728) * np.cosh(np.cosh(np.arctan(1.9423158330970622))) - (np.square(x[0]) * np.rint(-2.065621497047198) + 3.503326125821749 / np.reciprocal(x[2]) + x[1] * np.square(x[1]))
```

### Problem 4

**MSE**: 3.0653052503693838e-06

```python
3.3325688447227532 + (np.cos(x[1]) / 0.1428298184783164) - ((-0.5653322717250981 - x[0]) / -10.9872282724623779)
```

### Problem 5

**MSE**: 1.1822644703340634e-20

```python
((2.467100421154991e-12 * (np.power(4.18958630424536, (3.017249747918303 - x[1])) - 4.084409304778444)) * np.power(x[0], x[1]))
```

### Problem 6

**MSE**: 1.772934170781065e-08

```python
(x[1] - (((-3.7176133491516232 * x[0]) + (3.7181064589095936 * x[1])) / (np.minimum(4.381559519733427, -3.803901432200341) - np.cbrt(3.7181064589095936))))
```

### Problem 7

**MSE**: 194.70615387010136

```python
((np.sin((-4.287237004344295 - (x[0] - x[1]))) + np.sin(np.power(1556.6675533539744, (x[0] - x[1])))) * (np.exp((1.6053878748495762 + (x[0] * x[1]))) * np.sin((2232.504710869893 + (x[0] - x[1])))))
```

### Problem 8

**MSE**: 7752.954419575954

A high value and an anything but compact formula that suggest the algorithm’s inability to capture the underlying relationship between the input and output variables. This may indicate that the chosen model is not suited to the problem, that the dataset contains significant noise, or that further tuning and feature selections are needed to improve performance. Perhaps a more compact formula with a slightly higher MSE would have been preferable (*e.g.* a short formula with an MSE on the order of 100_000), but it was decided to report the one with the lowest MSE, despite its complexity. Future work could explore alternative models to balance accuracy and interpretability more effectively.

```python
np.minimum(np.sinh(x[5]) * np.maximum(9.3067551639483366, x[0] / x[0] - 8.1737401391616195) * np.maximum(np.maximum(np.minimum(np.cosh(x[5]), 18.4423895407085805), np.minimum(np.square(x[5]), 15.037856692023084)), np.minimum(17.6972179719256010, np.square(x[5])) + np.minimum(np.square(x[5]), np.absolute(x[5]))) + np.minimum(np.sinh(x[4]) * np.maximum(37.0927078418996027, x[3]), np.maximum(np.sinh(x[5]), 9.720508873329518) / 2.564537561212518 + np.sinh(x[4]) * -36.5491997365694977) - np.minimum(np.maximum(np.remainder(np.power(np.maximum(3.025150828938454, np.sin(x[1])), np.remainder(x[4], -4.190526875841163) + 2.5852944295947005), np.minimum(np.sinh(x[4]) + np.sinh(x[5]), np.minimum(6.530635069831985, x[2]) - 15.751711154922196)), np.maximum(-39.1515397544814214, 314.8402983836045133 / np.maximum(-4.933777461347297, x[3])) + (np.maximum(-9.174199129628121, x[3]) * np.exp(4.583029845151287)) / -1.5537384634524341), np.remainder(np.maximum(100.0199410769763602 / (x[3] - 2.1332481808545545), -32.7772659233697216), np.minimum(36.7506213572168948 * np.cosh(x[5]), -4.109412935321963 * np.maximum(-9.62084356692828, x[3])) * 17.361335511767116)), np.minimum(np.maximum(9.174199129628121, x[3]) + np.sinh(x[5]), np.cosh(x[5]) + np.cos(x[5])) * np.minimum(9.720508873329518, np.square(x[5])) + np.minimum(4.583029845151287, np.absolute(x[5])) + np.maximum(44.8278193425921329 / np.absolute(x[5]), np.absolute(x[5]) + 6.695358044391064) * np.maximum(np.sinh(x[5]) + np.cos(x[5]), -0.7294152703515632) * 8.680667755883558 - np.minimum(np.square(np.maximum(-4.109412935321963 * np.sinh(x[5]), np.minimum(17.6972179719256010, np.square(x[5])) + np.minimum(np.square(x[5]), np.absolute(x[5])) )), np.square(np.minimum(np.maximum(np.maximum(np.sinh(x[5]), -7.8797548932089201), np.minimum(np.square(x[5]), np.absolute(x[5]))), np.sinh(x[5]) +  0.6904692721820371 ))))
```

## Contributors
<table>
  <tr>
    <td align="center">
      <a href="https://github.com/AgneseRe">
        <img src="https://github.com/AgneseRe.png" width="50px" style="border-radius: 50%; border: none;" alt=""/>
        <br />
        <sub>AgneseRe</sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/FerraiuoloP">
        <img src="https://github.com/FerraiuoloP.png" width="50px" style="border-radius: 50%; border: none;" alt=""/>
        <br />
        <sub>FerraP</sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/GDennis01">
        <img src="https://github.com/GDennis01.png" width="50px" style="border-radius: 50%; border: none;" alt=""/>
        <br />
        <sub>GDennis01</sub>
      </a>
    </td>
    <td align="center" style="border: none;">
      <a href="https://github.com/XhoanaShkajoti">
        <img src="https://github.com/XhoanaShkajoti.png" width="50px" style="border-radius: 50%; border: none;" alt=""/>
        <br />
        <sub>XhoanaShkajoti</sub>
      </a>
    </td>
  </tr>
</table>

## License
This project is licensed under the MIT License.
