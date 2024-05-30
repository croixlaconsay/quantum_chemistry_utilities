#!/usr/bin/env python
# coding: utf-8

# # IRC Parse

# A tool for automating the parsing of Gaussian output files (.out or .log) of Intrinsic Reaction Coordinate (IRC) calculations. For information on IRC calculations see: https://gaussian.com/irc/. 
# 
# Required inputs: a Gaussian '09 or '16 IRC output file.
# 
# Expected outputs: individual XYZ-formatted files (named molecule1.xyz, molecule2.xyz, and so on). These XYZ files can be used for subsequent analysis/calculations (e.g,. single-point energy corrections, etc.)
# 
# Limitations: the Gaussian IRC algorithm will start from the transition structure and obtain IRC points from that structure on. This implies that the resulting XYZ files will not be in a structured order, but not necessarily evolve from reactants to products or vice versa.
# 
# Caveats:
# • If you use 'forward' or 'reverse' in your IRC calculation, then the code will work only work within those constraints.
# • The transition structure will not be present in the resuling XYZ files. You must create a separate XYZ file for the transition structure.

# In[2]:


# import modules
import matplotlib as pyplot
import pandas as pd
import os
import re


# In[3]:


def parse_out_file(file_name):
    """
    Defines a function that parses number of atoms and XYZ coordinates

    Args:
        file_name: A Gaussian output file.

    Returns:
        output_lines (list): content parsed from output file to be used in the next function.
        natoms (int): number of atoms.
    """
    with open(file_name, 'r') as f:
        lines = f.readlines()

    output_lines = [] # initialize a list called output_lines
    natoms = 0 # Initialize number of atoms and set to 0
    start_appending = False  # Initialize the flag
    
    """
    Iterate through each line to find 'NAtoms'.
    Update number of atoms and then find 'Input orientation'.
    Append all coordinates for each instance of 'Input orientation' to output_lines.
    """
    for i, line in enumerate(lines):
        match = re.match(r'\s*NAtoms\s*=\s*(\d+)', line)
        if match:
            natoms = int(match.group(1))

        if 'Input orientation' in line:
            start_appending = True
            start_line = i + 5  # Start appending from the 5th line after 'Input orientation'
            end_line = start_line + natoms + 1  # Stop appending after natoms + 1 lines

            # Append lines from start_line to end_line
            for j in range(start_line, end_line):
                if j < len(lines):
                    output_lines.append(lines[j])

            start_appending = False  # Reset the flag

    return output_lines, natoms


# In[4]:


def gen_xyz_file(output_lines):
    """
    Define a function that processes output_lines and 
    creates an xyz file that can be processed further 
    for input file generation
    """
    
    # Initialize two lists to store sublists of lines
    # for each molecule
    molecule_data = []
    current_molecule = []
    
    # Skip the first line
    output_lines = output_lines[1:]

    # Search output_lines for "---" and use this as a marker
    # for a new molecule
    for line in output_lines:
        if line.strip() == "---------------------------------------------------------------------":
            if current_molecule:
                molecule_data.append(current_molecule)
                current_molecule = []
        else:
            columns = line.strip().split()
            current_molecule.append([columns[1]] + columns[-3:])

    if current_molecule:
        molecule_data.append(current_molecule)
    
    # Use the number of atoms in the molecule to write an .xyz
    # file that contains the atom types and xyz coordinates
    for i, molecule in enumerate(molecule_data, start=1):
        num_atoms = len(molecule)
        title = f"molecule{i}"
        coords = molecule

        filename = f"{title}.xyz"
        with open(filename, "w") as f:
            f.write(f"{num_atoms}\n")
            f.write(f"{title}\n")
            for line in coords:
                f.write(f"{' '.join(line)}\n")

    print(f"Generated {len(molecule_data)} XYZ files.")


# In[5]:


"""
Prompt user to specify the Gaussian IRC file to parse.
Open the file.
"""

# Prompt the user to input the name of their file
file_name = input("Enter the name of your .out file: ")

# Open the file
with open(file_name, 'r') as f:
    lines = f.readlines()


# In[6]:


# Apply parse_out_file function on file.
output_lines, natoms = parse_out_file(file_name)

for line in output_lines:
    print(line.strip())


# In[7]:


# Use gen_xyz_file function on output_lines
xyz_file = gen_xyz_file(output_lines)

