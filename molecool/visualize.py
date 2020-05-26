"""
Functions for visualization. 
"""

import numpy as np
import matplotlib.pyplot as plt

def draw_molecule(coordinates, symbols, draw_bonds=None, save_location=None, dpi=300):
    """
    Draw a picture of the molecule.

    Parameters
    ----------
    coordinates : array
        Array with all the molecule's atoms.

    symbols : list
        List of strings containing atomic symbols.

    draw_bonds : list
        Specifies which bonds to be drawn (?)

    save_location : string, optional
        File path for saving histogram.

    dpi : integer, optional
        Resolution specification as dots per square inch of display.

    Returns
    -------
    ax : figure
        A figure representing the molecule.

    """    
    # Draw a picture of a molecule using matplotlib.
    
    # Throwing exceptions
    if len(coordinates) != len(symbols):
        raise Exception("The number of atomic positions and the number of atomic symbols DO NOT match.")
    
    # Create figure
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Get colors - based on atom name
    colors = []
    for atom in symbols:
        colors.append(atom_colors[atom])
    
    size = np.array(plt.rcParams['lines.markersize'] ** 2)*200/(len(coordinates))

    ax.scatter(coordinates[:,0], coordinates[:,1], coordinates[:,2], marker="o",
               edgecolors='k', facecolors=colors, alpha=1, s=size)
    
    # Draw bonds
    if draw_bonds:
        for atoms, bond_length in draw_bonds.items():
            atom1 = atoms[0]
            atom2 = atoms[1]
            
            ax.plot(coordinates[[atom1,atom2], 0], coordinates[[atom1,atom2], 1],
                    coordinates[[atom1,atom2], 2], color='k')
    
    # Save figure
    if save_location:
        plt.savefig(save_location, dpi=dpi, graph_min=0, graph_max=2)
    
    return ax

def bond_histogram(bond_list, save_location=None, dpi=300, graph_min=0, graph_max=2):
    """
    Draw a histogram of bond lengths.

    Parameters
    ----------
    bond_list : list
        List containing all bond lengths.
        
    save_location : string, optional
        File path for saving histogram.

    dpi : integer, optional
        Resolution specification as dots per square inch of display.

    graph_min : integer
        Minimum integer value on y-axis. 

    graph_max : integer
        Maximum integer value on y-axis.

    Returns
    -------
    ax : histogram
        A histogram representation of all bond lengths.

    """

    # Draw a histogram of bond lengths based on a bond_list (output from build_bond_list function)
        
    lengths = []
    for atoms, bond_length in bond_list.items():
        lengths.append(bond_length)
    
    bins = np.linspace(graph_min, graph_max)
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    plt.xlabel('Bond Length (angstrom)')
    plt.ylabel('Number of Bonds')
    
    
    ax.hist(lengths, bins=bins)
    
    # Save figure
    if save_location:
        plt.savefig(save_location, dpi=dpi)
    
    return ax
