# RPG Character Optimization using Genetic Algorithms

## Problem Description

In this project, our goal is to optimize character configurations for a role-playing game (RPG) using a genetic algorithm engine. The game features four character classes: Warriors, Archers, Defenders, and Assassins, each with distinct performance objectives in terms of attack and defense. Characters can equip items with specific attributes, and the goal is to optimally allocate 150 attribute points among Strength, Agility, Expertise, Resistance, and Health for each character.

### Character Classes

1. **Warrior**: Balances attack and defense.
   - Performance = 0.6 * Attack + 0.4 * Defense

2. **Archer**: Prioritizes attack over defense.
   - Performance = 0.9 * Attack + 0.1 * Defense

3. **Defender**: Focuses on defense to protect allies.
   - Performance = 0.1 * Attack + 0.9 * Defense

4. **Infiltrator**: Emphasizes attack and some defense.
   - Performance = 0.8 * Attack + 0.3 * Defense

### Equipment

Items have attributes such as Strength, Agility, Expertise, Resistance, and Health. The allocation of 150 points among these attributes affects character performance.

### Size

Character size affects attack and defense modifiers.

### Attack

Attack and defense are determined using specific formulas for each character class.

## Implemented Methods

The genetic algorithm engine implements the following methods:

### Genetic Operators

- **Crossover**: 
  - Single-Point Crossover
  - Two-Point Crossover
  - Uniform Crossover
  - Annular Crossover

- **Mutation**:
  - Single Gene Mutation
  - Multi-Gene Mutation
  - Uniform Mutation
  - Non-Uniform Mutation (optional)

### Selection and Replacement

- **Selection Methods**:
  - Elite Selection
  - Roulette Selection
  - Universal Selection
  - Boltzmann Selection
  - Tournament Selection (both versions)
  - Ranking Selection

- **Replacement Methods**:
  - Elite Replacement
  - Roulette Replacement
  - Universal Replacement
  - Boltzmann Replacement
  - Tournament Replacement (both versions)
  - Ranking Replacement

### Termination Criteria

- Maximum Number of Generations
- Structure-Based Termination
- Content-Based Termination
- Proximity to an Optimum (configurable)

### Configuration

The program reads configuration parameters from an external file, allowing customization of genetic operators, selection methods, replacement methods, and termination criteria.



