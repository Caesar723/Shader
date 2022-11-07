import numpy as np


def points(args,n):
    

    ini="""
<init steps="1">

<step 1>
    {}
    <window>
        hsrmode="3"
        nomidpts="true"
        anaglyph="-1"
        transparent="false"
        alpha="140"
        twoViews="false"
        unlinkViews="false"
        axisExtension="0.7"
        showNormals="false"
        showNormalsAtPts="false"
        xaxislabel="x"
        yaxislabel="y"
        zaxislabel="z"
        xmin="-2"
        xmax="2"
        xscale="1"
        xscalefactor="1"
        ymin="-2"
        ymax="2"
        yscale="1"
        yscalefactor="1"
        zmin="-2"
        zmax="2"
        zscale="1"
        zscalefactor="1"
        zminClip="-4"
        zmaxClip="4"
        edgesOn="true"
        facesOn="true"
        showBox="true"
        showAxes="true"
        showTicks="true"
        perspective="true"
        centerxpercent="0.5"
        centerypercent="0.5"
        rotationsteps="30"
        autospin="true"
        xygrid="false"
        yzgrid="false"
        xzgrid="false"
        gridsOnBox="true"
        gridPlanes="false"
        gridColor="rgb(128,128,128)"
        traceMode="0"
        keep2D="false"
        zoom="0.968235"
    </window>
    <viewpoint>
        center="8.236391035463319,4.755282581475766,3.0901699437494745,1"
        focus="0,0,0,1"
        up="0,0,2,1"
    </viewpoint>
</step>
    """
    text=""
    for i in args:
        print(str(np.reshape(i,(1,3))))
        tex="""
    <point>
        point="({})"
        color="rgb{}"
        size="4"
        visible="true"
    </point>
        """
        tex=tex.format(str([ii for ii in np.reshape(np.array(i),(1,3))[0]])[1:-1],i[1])
        #print(type(i))
        text+=tex

    res=ini.format(text)
    with open(f"script{n}.txt",'w') as f:
        f.write(res)

#points([np.array([1,2,3]),np.array([3,2,3])])

def planes(args):
    

    ini="""
<init steps="1">

<step 1>
    {}
    <window>
        hsrmode="3"
        nomidpts="true"
        anaglyph="-1"
        transparent="false"
        alpha="140"
        twoViews="false"
        unlinkViews="false"
        axisExtension="0.7"
        showNormals="false"
        showNormalsAtPts="false"
        xaxislabel="x"
        yaxislabel="y"
        zaxislabel="z"
        xmin="-2"
        xmax="2"
        xscale="1"
        xscalefactor="1"
        ymin="-2"
        ymax="2"
        yscale="1"
        yscalefactor="1"
        zmin="-2"
        zmax="2"
        zscale="1"
        zscalefactor="1"
        zminClip="-4"
        zmaxClip="4"
        edgesOn="true"
        facesOn="true"
        showBox="true"
        showAxes="true"
        showTicks="true"
        perspective="true"
        centerxpercent="0.5"
        centerypercent="0.5"
        rotationsteps="30"
        autospin="true"
        xygrid="false"
        yzgrid="false"
        xzgrid="false"
        gridsOnBox="true"
        gridPlanes="false"
        gridColor="rgb(128,128,128)"
        traceMode="0"
        keep2D="false"
        zoom="0.968235"
    </window>
    <viewpoint>
        center="8.236391035463319,4.755282581475766,3.0901699437494745,1"
        focus="0,0,0,1"
        up="0,0,2,1"
    </viewpoint>
</step>
    """
    text=""
    for plane in args:
        for i in plane.p:
            print(str(np.reshape(i,(1,3))),plane.color)
            tex="""
        <point>
            point="({})"
            color="rgb{}"
            size="4"
            visible="true"
        </point>
            """
            tex=tex.format(str([ii for ii in np.reshape(np.array(i),(1,3))[0]])[1:-1],plane.color)
            #print(type(i))
            text+=tex

    res=ini.format(text)
    with open("script.txt",'w') as f:
        f.write(res)
