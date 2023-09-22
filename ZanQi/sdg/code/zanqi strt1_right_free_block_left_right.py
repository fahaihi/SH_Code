# import replicator envirnoment 
import omni.replicator.core as rep

# setup random view range for camera: low point, high point
camera_pos = [(20,3,18)]

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
                position=(20,0,15),
                rotation=(0,-90,-90),
                scale=rep.distribution.uniform(.05,.05,0.05)
                )
        with jetbot:
            rep.modify.pose(
                position=(20,1,20),
                rotation=(-90,90,0),
                scale=rep.distribution.uniform(3,3,3)
                ) 

        
# define function to create random position range for target  
        def get_shapes1():
            shapes = rep.get.prims(semantics=[('class', 'track')])
            with shapes:
                rep.modify.pose(
                    position=rep.distribution.uniform((0, 0, -2500), (0, 00,3000)))
            return shapes.node
        rep.randomizer.register(get_shapes1)


# Setup camera and attach it to render product
        camera = rep.create.camera(
                         position=camera_pos[0], 
                         focal_length=8,
#Changing Y angle from 0 to 225 for left turn scenario
#Changing Y angle from 0 to 135 for right turn scenario
#Changing Y angle=180 for free/block scenario
                         rotation=(160, 135, 180)
                         )
        render_product = rep.create.render_product(camera, resolution=(1024, 1024))

        with rep.trigger.on_frame(num_frames=100): #number of picture
               rep.randomizer.get_shapes1()


# Initialize and attach writer for basic format data 
        writer = rep.WriterRegistry.get("BasicWriter")
        writer.initialize(
                 output_dir="c:/sdg/straight1right/free at straight1right", rgb=True
               )
        writer.attach([render_product])
        rep.orchestrator.preview()