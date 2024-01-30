# mess-model

The purpose of the Agent Based Modelling is to
1. explore how the irrigation-related agents and their related environment interact with each
other;
1. test the decision-making mechanisms from individual level and collective level in an irrigation
system; and
1. study how short-term irrigation management actions create long-term irrigation system
patterns.

The environment of this simulation is a water system: one main river brings water to an irrigation
system with farmers with their farmlands, canals, and gates. The model consists of the following
entities: river, canals, gates, farmlands, barley, virtual water managers, and farmers. The entities
and their state variables are defined as follows:
1. The river is the origin of the water resource. Water moves one cell per time step, whatever the
inflow. The relevant variable is varied river discharges.
1. Canals are built along the river. Canals are transfer tools of water, transporting water from the
river to farmers. Water moves one cell per time step, organized with canal capacity.
1. Gates allow water to flow from the river into irrigation canals, and from canals to farm(s).
There are gates at the junction of the river and canals or two canals (head gates), and at the
junction of canals and farms (farmers’ gate). Gates control the water flow – either from river
to canals or from canals to farmers. Water moves one cell per time step, arranged by gate
capacity.
1. There are two types of farmlands in IRABMs: one farmland type is with barley; another one is
fallow – preparing for the next crop season. The farmlands with barley have the variables:
water demand, water stress, start barley, barley yields, harvest cycle, barley alive or not. The
fallow farmlands have the variable: available for barley sowing, pre-irrigation demand when
they are ready for the next cultivation.
1. Virtual water managers propose water (re)allocation strategies. Water allocation control, or
irrigation water control, to canals, can be done in two ways – time control and demand control
(IRABM). In AIRABM, water managers can redistribute water among farmers along the same
canal, while water managers can control the irrigation system dynamics based on the harvest
situation in IRABM3 as well. Water distribution strategies are shaped through river discharge,
gate capacity, the number of canals irrigated simultaneously, and barley water demands.
1. The farmers make choices on crop growing and sowing choice in the next year (farmlands
dynamics). Farmers will support the water allocation strategies in the system. They have the
variable: irrigation demand.
1. Barley yields update annually and are based on the supplied water throughout the season.
Barley yields and farmlands dynamics at farms (the smallest spatial scale, representing
individual farmers or families) are used to check results of water distribution, individual
farmers’ planting choices, and the collective decision-making on water relocation to upstream,
middle stream, and downstream farmers. Aggregating yields at the levels of individual
farmers, canals, or whole system allows for exploring how specific irrigation strategies create
patterns in water availability and yields. The system dynamics – farmers/canals movement or
expansion is used to explore how the short-term actions promote longer-term patterns.
