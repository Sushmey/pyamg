import matplotlib.pyplot as plt

import numpy as np
import shapely.geometry as sg
from shapely.ops import cascaded_union
import matplotlib
import pyamg

def plotaggs(AggOp, V, E, G, ax, fig,
             aggvals=None,
             vmin=None, vmax=None, cmapname='cool',
             **kwargs):
    """
    Parameters
    ----------
    AggOp : CSR sparse matrix
        n x nagg encoding of the aggregates AggOp[i,j] == 1 means node i is in aggregate j
    V : ndarray
        n x 2 coordinate array of the mesh
    E : ndarray
        nel x 3 index array of the mesh elements
    G : CSR sparse matrix
        n x n connectivity matrix for the vertices
    ax : axis
        matplotlib axis
    """

    cmap = plt.get_cmap(cmapname)
    if aggvals is not None:
        if not vmax or not vmin:
            vmax = min(aggvals)
            vmax = max(aggvals)
        norm = matplotlib.colors.Normalize(vmin=0, vmax=vmax)
        aggcolor=[cmap(norm(v)) for v in aggvals]

    # plot the mesh
    # ax.triplot(V[:,0], V[:,1], E, color='0.5', lw=1.0)

    # plot the markers
    # ax.plot(V[:,0],V[:,1], 's', ms=5, markeredgecolor='w', color='tab:red')
    # for i in range(V.shape[0]):
    #     ax.text(V[i,0], V[i,1], f'{i}')

    for aggnum, agg in enumerate(AggOp.T):                                    # for each aggregate
        aggids = agg.indices                               # get the indices

        todraw = []                                        # collect things to draw
        if len(aggids) == 1:
            i = aggids[0]
            coords = (V[i, 0], V[i,1])
            newobj = sg.Point(coords)
            todraw.append(newobj)

        for i in aggids:                                   # for each point in the aggregate
            nbrs = G.getrow(i).indices                     # get the neighbors in the graph

            for j1 in nbrs:                                # for each neighbor
                found = False                              # mark if a triad ("triangle") is found
                for j2 in nbrs:
                    if (j1!=j2 and i!=j1 and i!=j2 and     # don't count i - j - j as a triangle
                        j1 in aggids and j2 in aggids and  # j1/j2 are in the aggregate
                        G[j1,j2]                           # j1/j2 are connected
                       ):
                        found = True                       # i - j1 - j2 are in the aggregate
                        coords = list(zip(V[[i,j1,j2], 0], V[[i,j1,j2],1]))
                        todraw.append(sg.Polygon(coords))  # add the triangle to the list
                if not found and i!=j1 and j1 in aggids:   # if we didn't find a triangle, then ...
                    coords = list(zip(V[[i,j1], 0], V[[i,j1],1]))
                    newobj = sg.LineString(coords)         # add a line object to the list
                    todraw.append(newobj)

        todraw = cascaded_union(todraw)                    # union all objects in the aggregate
        todraw = todraw.buffer(0.1)                        # expand to smooth
        todraw = todraw.buffer(-0.05)                      # then contract

        try:
            xs, ys = todraw.exterior.xy                    # get all of the exterior points
            if aggvals is not None:
                kwargs['color'] = aggcolor[aggnum]
            ax.fill(xs, ys,
                    **kwargs,
                    clip_on=False)                         # fill with a color
        except:
            pass                                           # don't plot certain things (singletons)

    plt.colorbar(plt.cm.ScalarMappable(norm=norm, cmap=cmap), ax=ax)

    #c_map_ax = fig.add_axes([0.0, 1.1, 1.0, 0.02])
    #cb1 = matplotlib.colorbar.ColorbarBase(c_map_ax,
    #                            ticks = np.linspace(0, vmax, 10),
    #                            cmap=cmap,
    #                            norm=norm,
    #                            orientation='horizontal')
    ax.set_aspect('equal')