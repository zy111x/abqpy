from __future__ import annotations

from abqpy.decorators import abaqus_class_doc

from ..UtilityAndView.abaqusConstants import ON, Boolean, SymbolicConstant
from .InteractionState import InteractionState


@abaqus_class_doc
class CavityRadiationState(InteractionState):
    """The CavityRadiationState object stores the propagating data for a CavityRadiation object. One instance of
    this object is created internally by the CavityRadiation object for each step. The instance is also deleted
    internally by the CavityRadiation object. The CavityRadiationState object has no constructor or methods. The
    CavityRadiationState object is derived from the InteractionState object.

    .. note::
        This object can be accessed by::

            import interaction
            mdb.models[name].steps[name].interactionStates[name]

        The corresponding analysis keywords are:

        - RADIATION VIEWFACTOR
    """

    #: A SymbolicConstant specifying the blocking checks to be performed in the viewfactor
    #: calculations. Possible values are BLOCKING_ALL, NO_BLOCKING, and PARTIAL_BLOCKING.
    blocking: SymbolicConstant

    #: A SymbolicConstant specifying the propagation state of the blocking member. Possible
    #: values are UNSET, SET, UNCHANGED, and FREED.
    blockingState: SymbolicConstant

    #: A SymbolicConstant specifying the propagation state of the **blockingSurfaces** member.
    #: Possible values are UNSET, SET, UNCHANGED, and FREED.
    blockingSurfacesState: SymbolicConstant

    #: A Float specifying the distance beyond which factors need not be calculated because
    #: surfaces are judged to be too far apart to “see” each other (due to blocking by other
    #: surfaces).
    rangeOfView: float | None = None

    #: A SymbolicConstant specifying the propagation state of the **rangeOfView** member.
    #: Possible values are UNSET, SET, UNCHANGED, and FREED.
    rangeOfViewState: SymbolicConstant

    #: A Boolean specifying whether reflection must be included in the cavity radiation
    #: calculations. The default value is ON.
    surfaceReflection: Boolean = ON

    #: A SymbolicConstant specifying the propagation state of the **surfaceReflection** member.
    #: Possible values are UNSET, SET, UNCHANGED, and FREED.
    surfaceReflectionState: SymbolicConstant

    #: A Float specifying the acceptable tolerance for the viewfactor calculations.
    viewfactorAccuracyTol: float | None = None

    #: A SymbolicConstant specifying the propagation state of the **viewfactorAccuracyTol**
    #: member. Possible values are UNSET, SET, UNCHANGED, and FREED.
    viewfactorAccuracyTolState: SymbolicConstant

    #: A tuple of Strings specifying the surfaces that provide blocking inside the cavity.
    blockingSurfaces: tuple[str, ...] = ()

    #: A SymbolicConstant specifying the propagation state of the InteractionState object.
    #: Possible values
    #: are:NOT_YET_ACTIVECREATEDPROPAGATEDMODIFIEDDEACTIVATEDNO_LONGER_ACTIVETYPE_NOT_APPLICABLEINSTANCE_NOT_APPLICABLEBUILT_INTO_BASE_STATE
    status: SymbolicConstant
