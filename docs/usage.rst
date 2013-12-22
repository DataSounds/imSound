========
Usage
========

To use imSound in a project:

.. code-block:: python 

    from imSound import imSound
    import numpy as np

    data = np.random.rand(100).reshape(10,10)
    data_fig = imSound.ImageSound(data)
    data_fig.play_move()

A figure is generated internally with `matplotlib <http://matplotlib.org/>`_ 
and coursing mouse will display sounds of data intensities.

