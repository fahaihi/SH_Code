# import replicator envirnoment 
import omni.replicator.core as rep

# setup random view range for camera: low point, high point
camera_pos = [(36,3,45)]

# setup working layer 
with rep.new_layer():

# define 3d models: usd format file source link, class, initial position  
        WORKSHOP = 'http://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Wood/Block_A/BlockPallet_A03_PR_NVD_01.usd'
        TRACK    = 'c:/sdg/model/trackfromfbxtousd.usd'
        CONE     = 'http://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/DigitalTwin/Assets/Warehouse/Safety/Cones/Heavy-Duty_Traffic/HeavyDutyTrafficCone_A06_91cm_PR_V_NVD_01.usd'
        JETBOT   = 'c:/sdg/model/jetbot.usd'
        
        workshop = rep.create.from_usd(WORKSHOP)
        track    = rep.create.from_usd(TRACK,semantics=[('class', 'track')])
        jetbot   = rep.create.from_usd(JETBOT)
        cone1    = rep.create.from_usd(CONE,semantics=[('class', 'block')])
        with workshop:
            rep.modify.pose(
                position=(-0, -25, 0),
                rotation=(0,-90,-90),
                scale=rep.distribution.uniform(2,2,2)
                )
        with track:
            rep.modify.pose(
                position=(20,0,0),
                rotation=(0,0,0),
                scale=rep.distribution.uniform(.01,.01,.01)
                )
        with cone1:
            rep.modify.pose(
                position=(34,-.60,47),
                rotation=(0,-90,-90),
                scale=rep.distribution.uniform(.05,.05,0.05)
                )
        with jetbot:
            rep.modify.pose(
                position=(37,1,44),
                rotation=(-90,229,0),
                scale=rep.distribution.uniform(3,3,3)
                ) 
        
# define function to create random position range for target  
        def get_shapes1():
            shapes = rep.get.prims(semantics=[('class', 'track')])
            with shapes:
                rep.modify.pose(
                    position=rep.distribution.sequence([(1595,0,400),(1635,0,360),(1675,0,320),(1715,0,280),(1755,0,240),(1795,0,200),(1835,0,160),(1875,0,120),(1915,0,80),(1955,0,40)],ordered=True ))
                    #position=rep.distribution.sequence([(1960,0,45),(1920,0,85),(1880,0,125),(1840,0,165),(1800,0,205),(1760,0,245),(1720,0,285),(1680,0,325),(1640,0,365),(1600,0,405)],ordered=True ))
            return shapes.node
        rep.randomizer.register(get_shapes1)


# Setup camera and attach it to render product
        camera = rep.create.camera(
                         position=camera_pos[0], 
                         focal_length=9,
#Changing Y angle to 100 for left scenario
#Y angle =45 for block & right scensrio
                         rotation=(160, 45, -180)
                         )
        render_product = rep.create.render_product(camera, resolution=(1024, 1024))

        with rep.trigger.on_frame(num_frames=10): #number of picture
            rep.randomizer.get_shapes1()


# Initialize and attach writer for Kitti format data 
        writer = rep.WriterRegistry.get("BasicWriter")
        writer.initialize(
                 output_dir="c:/sdg/turn1up/block at turn1up", rgb=True
               )
        writer.attach([render_product])
        rep.orchestrator.preview()