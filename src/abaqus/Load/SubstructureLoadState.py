from __future__ import annotations

from abqpy.decorators import abaqus_class_doc

from ..UtilityAndView.abaqusConstants import SymbolicConstant
from .LoadState import LoadState


@abaqus_class_doc
class SubstructureLoadState(LoadState):
    """The SubstructureLoadState object stores the propagating data for a substructure load in a step. One
    instance of this object is created internally by the SubstructureLoad object for each step. The instance is
    also deleted internally by the SubstructureLoad object. The SubstructureLoadState object has no constructor
    or methods. The SubstructureLoadState object is derived from the LoadState object.

    .. note::
        This object can be accessed by::

            import load
            mdb.models[name].steps[name].loadStates[name]

        The corresponding analysis keywords are:

        - SLOAD
    """

    #: A tuple of strings specifying the names of the load cases to be activated.
    loadCaseNames: tuple[str, ...] = ()

    #: A Float or a Complex specifying the load magnitude.
    magnitude: float | None = None

    #: A SymbolicConstant specifying the propagation state of the load magnitude. Possible
    #: values are UNSET, SET, UNCHANGED, and MODIFIED.
    magnitudeState: SymbolicConstant

    #: A SymbolicConstant specifying the propagation state of the **amplitude** member. Possible
    #: values are UNSET, SET, UNCHANGED, and FREED.
    amplitudeState: SymbolicConstant

    #: A SymbolicConstant specifying the propagation state of the LoadState object. Possible
    #: values are:
    #:
    #: - NOT_YET_ACTIVE
    #: - CREATED
    #: - PROPAGATED
    #: - MODIFIED
    #: - DEACTIVATED
    #: - NO_LONGER_ACTIVE
    #: - TYPE_NOT_APPLICABLE
    #: - INSTANCE_NOT_APPLICABLE
    #: - BUILT_INTO_BASE_STATE
    status: SymbolicConstant

    #: A String specifying the name of the amplitude reference. The String is empty if the load
    #: has no amplitude reference.
    amplitude: str = ""
