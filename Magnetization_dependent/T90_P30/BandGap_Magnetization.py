import plotly.graph_objects as go
import numpy as np
from scipy.interpolate import make_interp_spline

gap_phi=([0.000000000,0.0170500,0.025850000,0.035090000,0.023090000,0.011875400,0.000000000,0.011570700,0.022807000,0.033210,0.026778000,0.018908000,0.000000000,0.020213100,0.028547200,0.036078500,0.027443000,0.018746000,0.000000000,0.017505000,0.025066000,0.033600000,0.023099000,0.012020000,0.000000000,0.011588000,0.022824000,0.033290000,0.026781000,0.018916720,0.000000000,0.020213000,0.028530000,0.036767800,0.027446800,0.018748400,0.000000000])
gap_theta=([0.08899,0.0768,0.0637,0.0476349,0.0305487,0.01272,0.006419,0.023938,0.0218036,0,0.020597,0.0285723,0.01671,0.021353,0.0365,0.051,
0.06754,0.08159,0.09321,0.07685,0.064097,0.04756,0.03054,0.012712,0.0063,0.0243,0.021795,0,0.02051,0.02819,0.01669,0.01903,0.0359,0.05225,
0.06734,0.08241,0.08899])
angle = [0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,310,320,330,340,350,360]

polar_trace1 = go.Scatterpolar(r=gap_phi, theta=angle, mode='markers', marker=dict(color='yellow', size=14))
polar_trace3 = go.Scatterpolar(r=gap_phi, theta=angle, mode='lines',line=dict(width=2), marker=dict(color='black', size=15))
cartesian_trace = go.Scatter( x=[0],  y=[0], mode='markers',  marker=dict(color='grey'))

batasplot=5
bp=0
batasplo=int(batasplot)
gr=16


layout = go.Layout(
       paper_bgcolor='rgba(0,0,0,0)',
       plot_bgcolor='rgba(0,0,0,0)',
       showlegend=False,
       font=dict(
       family='serif',
          size=45 ,color='black', ),
       # title=f'ΔE vs φ',
       polar=dict(
          bgcolor = "rgba(255, 255, 255, 0.2)",

          radialaxis=dict(
              visible=True,
              range=[0,0.6],
              #range=[-0.2,6.4],
              #tickvals=np.linspace(bp,batasplot,9),
              showticklabels=False,
              showline=False,     # Show axis line
              ticklen=0,
              tickmode='linear', tick0=0 ,  dtick=0.2,
              gridwidth=3,
              gridcolor='lightgrey'),
          angularaxis=dict(
              visible=True,
              direction='counterclockwise',
              rotation=0,
              #tick0 = 0.1, dtick = "L0.5",
              gridwidth=3,
              tickmode='linear', tick0=0 ,  dtick=30,
              linewidth=4,
              tickwidth=4,
              ticklen=10,
              gridcolor='lightgrey')
      ),
       yaxis=dict(
           range=[-4, 4],
           #range=[-0.6,0.6],
           #title=(f'ΔE ( μeV / u.c. )'),
           #title = ('ΔE (meV)'),
           title = ('Eg (meV)'),
          #title=(f"Chern Number"),
          #title=(f 'Chern Number'),
           anchor='free',
           position=0.17,
         # titlesize=25,
         # tickmode='linear', tick0=0 ,  dtick=0.6,
           #tickvals=[-100,-50,0,50,100],
           #ticktext=['100','50','0','50','100'],
           #tickvals=[-0.6,-0.4,-0.2,0.0,0.2,0.4,0.6],
           #ticktext=['600','400','200','0','200','400','600'],
           tickvals=[-4,-2,0,2,4],
           ticktext=[100,50,0,50,100],
           #ticktext=['6.0','4.0','2.0','0.0','2.0','4.0','6.0'],
           #tickvals=[-0.97,0,0.97],
           #ticktext=[1,0,1],
       #   ticklen=15,
       #   ticks='inside',
          zeroline=False,
          showline=True,
          linewidth=4,
          tickwidth=4,
          gridcolor= 'rgba(0,0,0,0)'
          ),
      #yaxis=dict(visible=False),
      xaxis=dict(
          visible=False ),
        width=1000,
        height=1000
  )

  # Create the figure and add both traces
fig = go.Figure(layout=layout)
fig.add_trace(cartesian_trace)

fig.add_trace(polar_trace3)
fig.add_trace(polar_trace2)
#fig.add_trace(polar_trace1)
#fig.add_trace(polar_trace4)

fig.update_layout(template=None)

# Display the plot
fig.update_layout(width=1200, height=600)
fig.write_image("BandGap_.png")
fig.show()


