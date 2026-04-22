import plotly.graph_objects as go

class Visualizer:
    @staticmethod
    def render_3d_nexus(points):
        """心理スコアを座標にした3D銀河の生成"""
        fig = go.Figure(data=[go.Scatter3d(
            x=[p['x'] for p in points], y=[p['y'] for p in points], z=[p['z'] for p in points],
            mode='markers+lines',
            marker=dict(
                size=[p.get('size', 10) for p in points],
                color=[p['sentiment'] for p in points],
                colorscale='Magma',
                opacity=0.8
            ),
            line=dict(color='rgba(255,255,255,0.2)', width=1)
        )])
        fig.update_layout(
            paper_bgcolor='black',
            scene=dict(xaxis_visible=False, yaxis_visible=False, zaxis_visible=False),
            margin=dict(l=0, r=0, b=0, t=0)
        )
        return fig
