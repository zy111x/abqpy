from abaqusConstants import *
from .AnalysisStep import AnalysisStep
from ..Adaptivity.AdaptiveMeshConstraintState import AdaptiveMeshConstraintState
from ..Adaptivity.AdaptiveMeshDomain import AdaptiveMeshDomain
from ..BoundaryCondition.BoundaryConditionState import BoundaryConditionState
from ..Load.LoadCase import LoadCase
from ..Load.LoadState import LoadState
from ..PredefinedField.PredefinedFieldState import PredefinedFieldState
from ..StepMiscellaneous.Control import Control
from ..StepMiscellaneous.SolverControl import SolverControl
from ..StepOutput.DiagnosticPrint import DiagnosticPrint
from ..StepOutput.FieldOutputRequestState import FieldOutputRequestState
from ..StepOutput.HistoryOutputRequestState import HistoryOutputRequestState
from ..StepOutput.Monitor import Monitor
from ..StepOutput.Restart import Restart


class StaticStep(AnalysisStep):
    """The StaticStep object is used to indicate that the step should be analyzed as a static
    load step.
    The StaticStep object is derived from the AnalysisStep object.

    Attributes
    ----------
    name: str
        A String specifying the repository key.
    timePeriod: float
        A Float specifying the total time period. The default value is 1.0.
    nlgeom: Boolean
        A Boolean specifying whether to allow for geometric nonlinearity. The default value is
        OFF.
    stabilizationMethod: SymbolicConstant
        A SymbolicConstant specifying the stabilization type. Possible values are NONE,
        DISSIPATED_ENERGY_FRACTION, and DAMPING_FACTOR. The default value is NONE.
    stabilizationMagnitude: float
        A Float specifying the damping intensity of the automatic damping algorithm if the
        problem is expected to be unstable, and **stabilizationMethod** is not NONE. The default
        value is 2×10-4.
    adiabatic: Boolean
        A Boolean specifying whether to perform an adiabatic stress analysis. The default value
        is OFF.
    timeIncrementationMethod: SymbolicConstant
        A SymbolicConstant specifying the time incrementation method to be used. Possible values
        are FIXED and AUTOMATIC. The default value is AUTOMATIC.
    maxNumInc: int
        An Int specifying the maximum number of increments in a step. The default value is 100.
    initialInc: float
        A Float specifying the initial time increment. The default value is the total time
        period for the step.
    minInc: float
        A Float specifying the minimum time increment allowed. The default value is the smaller
        of the suggested initial time increment or 10-5 times the total time period.
    maxInc: float
        A Float specifying the maximum time increment allowed. The default value is the total
        time period for the step.
    matrixSolver: SymbolicConstant
        A SymbolicConstant specifying the type of solver. Possible values are DIRECT and
        ITERATIVE. The default value is DIRECT.
    matrixStorage: SymbolicConstant
        A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC,
        UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT.
    amplitude: SymbolicConstant
        A SymbolicConstant specifying the amplitude variation for loading magnitudes during the
        step. Possible values are STEP and RAMP. The default value is RAMP.
    extrapolation: SymbolicConstant
        A SymbolicConstant specifying the type of extrapolation to use in determining the
        incremental solution for a nonlinear analysis. Possible values are NONE, LINEAR, and
        PARABOLIC. The default value is LINEAR.
    noStop: Boolean
        A Boolean specifying whether to accept the solution to an increment after the maximum
        number of iterations allowed has been completed, even if the equilibrium tolerances are
        not satisfied. The default value is OFF.Warning:You should set **noStop=ON** only in
        special cases when you have a thorough understanding of how to interpret the results.
    useLongTermSolution: Boolean
        A Boolean specifying wether to obtain the fully relaxed long-term elastic solution with
        time-domain viscoelasticity or the long-term elastic-Plastic solution for two-layer
        viscoplasticity. The default value is OFF.
    solutionTechnique: SymbolicConstant
        A SymbolicConstant specifying the technique used to for solving nonlinear equations.
        Possible values are FULL_NEWTON and QUASI_NEWTON. The default value is FULL_NEWTON.
    reformKernel: int
        An Int specifying the number of quasi-Newton iterations allowed before the kernel matrix
        is reformed.. The default value is 8.
    convertSDI: SymbolicConstant
        A SymbolicConstant specifying whether to force a new iteration if severe discontinuities
        occur during an iteration. Possible values are PROPAGATED, CONVERT_SDI_OFF, and
        CONVERT_SDI_ON. The default value is PROPAGATED.
    adaptiveDampingRatio: float
        A Float specifying the maximum allowable ratio of the stabilization energy to the total
        strain energy and can be used only if **stabilizationMethod** is not NONE. The default
        value is 0.05.
    continueDampingFactors: Boolean
        A Boolean specifying whether this step will carry over the damping factors from the
        results of the preceding general step. This parameter must be used in conjunction with
        the **adaptiveDampingRatio** parameter. The default value is OFF.
    previous: str
        A String specifying the name of the previous step. The new step appears after this step
        in the list of analysis steps.
    description: str
        A String specifying a description of the new step. The default value is an empty string.
    fullyPlastic: str
        A String specifying the region being monitored for fully Plastic behavior. The default
        value is an empty string.
    explicit: SymbolicConstant
        A SymbolicConstant specifying whether the step has an explicit procedure type
        (**procedureType=ANNEAL**, DYNAMIC_EXPLICIT, or DYNAMIC_TEMP_DISPLACEMENT).
    perturbation: Boolean
        A Boolean specifying whether the step has a perturbation procedure type.
    nonmechanical: Boolean
        A Boolean specifying whether the step has a mechanical procedure type.
    procedureType: SymbolicConstant
        A SymbolicConstant specifying the Abaqus procedure. Possible values are:
        
        - ANNEAL
        - BUCKLE
        - COMPLEX_FREQUENCY
        - COUPLED_TEMP_DISPLACEMENT
        - COUPLED_THERMAL_ELECTRIC
        - DIRECT_CYCLIC
        - DYNAMIC_IMPLICIT
        - DYNAMIC_EXPLICIT
        - DYNAMIC_SUBSPACE
        - DYNAMIC_TEMP_DISPLACEMENT
        - COUPLED_THERMAL_ELECTRICAL_STRUCTURAL
        - FREQUENCY
        - GEOSTATIC
        - HEAT_TRANSFER
        - MASS_DIFFUSION
        - MODAL_DYNAMICS
        - RANDOM_RESPONSE
        - RESPONSE_SPECTRUM
        - SOILS
        - STATIC_GENERAL
        - STATIC_LINEAR_PERTURBATION
        - STATIC_RIKS
        - STEADY_STATE_DIRECT
        - STEADY_STATE_MODAL
        - STEADY_STATE_SUBSPACE
        - VISCO
    suppressed: Boolean
        A Boolean specifying whether the step is suppressed or not. The default value is OFF.
    fieldOutputRequestState: dict[str, FieldOutputRequestState]
        A repository of :py:class:`~abaqus.StepOutput.FieldOutputRequestState.FieldOutputRequestState` objects.
    historyOutputRequestState: dict[str, HistoryOutputRequestState]
        A repository of :py:class:`~abaqus.StepOutput.HistoryOutputRequestState.HistoryOutputRequestState` objects.
    diagnosticPrint: DiagnosticPrint
        A :py:class:`~abaqus.StepOutput.DiagnosticPrint.DiagnosticPrint` object.
    monitor: Monitor
        A :py:class:`~abaqus.StepOutput.Monitor.Monitor` object.
    restart: Restart
        A :py:class:`~abaqus.StepOutput.Restart.Restart` object.
    adaptiveMeshConstraintStates: dict[str, AdaptiveMeshConstraintState]
        A repository of :py:class:`~abaqus.Adaptivity.AdaptiveMeshConstraintState.AdaptiveMeshConstraintState` objects.
    adaptiveMeshDomains: dict[str, AdaptiveMeshDomain]
        A repository of :py:class:`~abaqus.Adaptivity.AdaptiveMeshDomain.AdaptiveMeshDomain` objects.
    control: Control
        A :py:class:`~abaqus.StepMiscellaneous.Control.Control` object.
    solverControl: SolverControl
        A :py:class:`~abaqus.StepMiscellaneous.SolverControl.SolverControl` object.
    boundaryConditionStates: dict[str, BoundaryConditionState]
        A repository of :py:class:`~abaqus.BoundaryCondition.BoundaryConditionState.BoundaryConditionState` objects.
    interactionStates: int
        A repository of :py:class:`~abaqus.Interaction.InteractionState.InteractionState` objects.
    loadStates: dict[str, LoadState]
        A repository of :py:class:`~abaqus.Load.LoadState.LoadState` objects.
    loadCases: dict[str, LoadCase]
        A repository of :py:class:`~abaqus.Load.LoadCase.LoadCase` objects.
    predefinedFieldStates: dict[str, PredefinedFieldState]
        A repository of :py:class:`~abaqus.PredefinedField.PredefinedFieldState.PredefinedFieldState` objects.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import step
        mdb.models[name].steps[name]

    The corresponding analysis keywords are:

    - STATIC
            - STEP
    """

    # A String specifying the repository key.
    name: str = ""

    # A Float specifying the total time period. The default value is 1.0.
    timePeriod: float = 1

    # A Boolean specifying whether to allow for geometric nonlinearity. The default value is
    # OFF.
    nlgeom: Boolean = OFF

    # A SymbolicConstant specifying the stabilization type. Possible values are NONE,
    # DISSIPATED_ENERGY_FRACTION, and DAMPING_FACTOR. The default value is NONE.
    stabilizationMethod: SymbolicConstant = NONE

    # A Float specifying the damping intensity of the automatic damping algorithm if the
    # problem is expected to be unstable, and **stabilizationMethod** is not NONE. The default
    # value is 2×10-4.
    stabilizationMagnitude: float = None

    # A Boolean specifying whether to perform an adiabatic stress analysis. The default value
    # is OFF.
    adiabatic: Boolean = OFF

    # A SymbolicConstant specifying the time incrementation method to be used. Possible values
    # are FIXED and AUTOMATIC. The default value is AUTOMATIC.
    timeIncrementationMethod: SymbolicConstant = AUTOMATIC

    # An Int specifying the maximum number of increments in a step. The default value is 100.
    maxNumInc: int = 100

    # A Float specifying the initial time increment. The default value is the total time
    # period for the step.
    initialInc: float = None

    # A Float specifying the minimum time increment allowed. The default value is the smaller
    # of the suggested initial time increment or 10-5 times the total time period.
    minInc: float = None

    # A Float specifying the maximum time increment allowed. The default value is the total
    # time period for the step.
    maxInc: float = None

    # A SymbolicConstant specifying the type of solver. Possible values are DIRECT and
    # ITERATIVE. The default value is DIRECT.
    matrixSolver: SymbolicConstant = DIRECT

    # A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC,
    # UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT.
    matrixStorage: SymbolicConstant = SOLVER_DEFAULT

    # A SymbolicConstant specifying the amplitude variation for loading magnitudes during the
    # step. Possible values are STEP and RAMP. The default value is RAMP.
    amplitude: SymbolicConstant = RAMP

    # A SymbolicConstant specifying the type of extrapolation to use in determining the
    # incremental solution for a nonlinear analysis. Possible values are NONE, LINEAR, and
    # PARABOLIC. The default value is LINEAR.
    extrapolation: SymbolicConstant = LINEAR

    # A Boolean specifying whether to accept the solution to an increment after the maximum
    # number of iterations allowed has been completed, even if the equilibrium tolerances are
    # not satisfied. The default value is OFF.Warning:You should set **noStop**=ON only in
    # special cases when you have a thorough understanding of how to interpret the results.
    noStop: Boolean = OFF

    # A Boolean specifying wether to obtain the fully relaxed long-term elastic solution with
    # time-domain viscoelasticity or the long-term elastic-Plastic solution for two-layer
    # viscoplasticity. The default value is OFF.
    useLongTermSolution: Boolean = OFF

    # A SymbolicConstant specifying the technique used to for solving nonlinear equations.
    # Possible values are FULL_NEWTON and QUASI_NEWTON. The default value is FULL_NEWTON.
    solutionTechnique: SymbolicConstant = FULL_NEWTON

    # An Int specifying the number of quasi-Newton iterations allowed before the kernel matrix
    # is reformed.. The default value is 8.
    reformKernel: int = 8

    # A SymbolicConstant specifying whether to force a new iteration if severe discontinuities
    # occur during an iteration. Possible values are PROPAGATED, CONVERT_SDI_OFF, and
    # CONVERT_SDI_ON. The default value is PROPAGATED.
    convertSDI: SymbolicConstant = PROPAGATED

    # A Float specifying the maximum allowable ratio of the stabilization energy to the total
    # strain energy and can be used only if **stabilizationMethod** is not NONE. The default
    # value is 0.05.
    adaptiveDampingRatio: float = 0

    # A Boolean specifying whether this step will carry over the damping factors from the
    # results of the preceding general step. This parameter must be used in conjunction with
    # the **adaptiveDampingRatio** parameter. The default value is OFF.
    continueDampingFactors: Boolean = OFF

    # A String specifying the name of the previous step. The new step appears after this step
    # in the list of analysis steps.
    previous: str = ""

    # A String specifying a description of the new step. The default value is an empty string.
    description: str = ""

    # A String specifying the region being monitored for fully Plastic behavior. The default
    # value is an empty string.
    fullyPlastic: str = ""

    # A SymbolicConstant specifying whether the step has an explicit procedure type
    # (*procedureType*=ANNEAL, DYNAMIC_EXPLICIT, or DYNAMIC_TEMP_DISPLACEMENT).
    explicit: SymbolicConstant = None

    # A Boolean specifying whether the step has a perturbation procedure type.
    perturbation: Boolean = OFF

    # A Boolean specifying whether the step has a mechanical procedure type.
    nonmechanical: Boolean = OFF

    # A SymbolicConstant specifying the Abaqus procedure. Possible values are:
    # - ANNEAL
    # - BUCKLE
    # - COMPLEX_FREQUENCY
    # - COUPLED_TEMP_DISPLACEMENT
    # - COUPLED_THERMAL_ELECTRIC
    # - DIRECT_CYCLIC
    # - DYNAMIC_IMPLICIT
    # - DYNAMIC_EXPLICIT
    # - DYNAMIC_SUBSPACE
    # - DYNAMIC_TEMP_DISPLACEMENT
    # - COUPLED_THERMAL_ELECTRICAL_STRUCTURAL
    # - FREQUENCY
    # - GEOSTATIC
    # - HEAT_TRANSFER
    # - MASS_DIFFUSION
    # - MODAL_DYNAMICS
    # - RANDOM_RESPONSE
    # - RESPONSE_SPECTRUM
    # - SOILS
    # - STATIC_GENERAL
    # - STATIC_LINEAR_PERTURBATION
    # - STATIC_RIKS
    # - STEADY_STATE_DIRECT
    # - STEADY_STATE_MODAL
    # - STEADY_STATE_SUBSPACE
    # - VISCO
    procedureType: SymbolicConstant = None

    # A Boolean specifying whether the step is suppressed or not. The default value is OFF.
    suppressed: Boolean = OFF

    # A repository of FieldOutputRequestState objects.
    fieldOutputRequestState: dict[str, FieldOutputRequestState] = dict[
        str, FieldOutputRequestState
    ]()

    # A repository of HistoryOutputRequestState objects.
    historyOutputRequestState: dict[str, HistoryOutputRequestState] = dict[
        str, HistoryOutputRequestState
    ]()

    # A DiagnosticPrint object.
    diagnosticPrint: DiagnosticPrint = DiagnosticPrint()

    # A Monitor object.
    monitor: Monitor = None

    # A Restart object.
    restart: Restart = Restart()

    # A repository of AdaptiveMeshConstraintState objects.
    adaptiveMeshConstraintStates: dict[str, AdaptiveMeshConstraintState] = dict[
        str, AdaptiveMeshConstraintState
    ]()

    # A repository of AdaptiveMeshDomain objects.
    adaptiveMeshDomains: dict[str, AdaptiveMeshDomain] = dict[str, AdaptiveMeshDomain]()

    # A Control object.
    control: Control = Control()

    # A SolverControl object.
    solverControl: SolverControl = SolverControl()

    # A repository of BoundaryConditionState objects.
    boundaryConditionStates: dict[str, BoundaryConditionState] = dict[
        str, BoundaryConditionState
    ]()

    # A repository of InteractionState objects.
    interactionStates: int = None

    # A repository of LoadState objects.
    loadStates: dict[str, LoadState] = dict[str, LoadState]()

    # A repository of LoadCase objects.
    loadCases: dict[str, LoadCase] = dict[str, LoadCase]()

    # A repository of PredefinedFieldState objects.
    predefinedFieldStates: dict[str, PredefinedFieldState] = dict[
        str, PredefinedFieldState
    ]()

    def __init__(
        self,
        name: str,
        previous: str,
        description: str = "",
        timePeriod: float = 1,
        nlgeom: Boolean = OFF,
        stabilizationMethod: SymbolicConstant = NONE,
        stabilizationMagnitude: float = None,
        adiabatic: Boolean = OFF,
        timeIncrementationMethod: SymbolicConstant = AUTOMATIC,
        maxNumInc: int = 100,
        initialInc: float = None,
        minInc: float = None,
        maxInc: float = None,
        matrixSolver: SymbolicConstant = DIRECT,
        matrixStorage: SymbolicConstant = SOLVER_DEFAULT,
        amplitude: SymbolicConstant = RAMP,
        extrapolation: SymbolicConstant = LINEAR,
        fullyPlastic: str = "",
        noStop: Boolean = OFF,
        maintainAttributes: Boolean = False,
        useLongTermSolution: Boolean = OFF,
        solutionTechnique: SymbolicConstant = FULL_NEWTON,
        reformKernel: int = 8,
        convertSDI: SymbolicConstant = PROPAGATED,
        adaptiveDampingRatio: float = 0,
        continueDampingFactors: Boolean = OFF,
    ):
        """This method creates a StaticStep object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].StaticStep

        Parameters
        ----------
        name
            A String specifying the repository key.
        previous
            A String specifying the name of the previous step. The new step appears after this step
            in the list of analysis steps.
        description
            A String specifying a description of the new step. The default value is an empty string.
        timePeriod
            A Float specifying the total time period. The default value is 1.0.
        nlgeom
            A Boolean specifying whether to allow for geometric nonlinearity. The default value is
            OFF.
        stabilizationMethod
            A SymbolicConstant specifying the stabilization type. Possible values are NONE,
            DISSIPATED_ENERGY_FRACTION, and DAMPING_FACTOR. The default value is NONE.
        stabilizationMagnitude
            A Float specifying the damping intensity of the automatic damping algorithm if the
            problem is expected to be unstable, and **stabilizationMethod** is not NONE. The default
            value is 2×10-4.
        adiabatic
            A Boolean specifying whether to perform an adiabatic stress analysis. The default value
            is OFF.
        timeIncrementationMethod
            A SymbolicConstant specifying the time incrementation method to be used. Possible values
            are FIXED and AUTOMATIC. The default value is AUTOMATIC.
        maxNumInc
            An Int specifying the maximum number of increments in a step. The default value is 100.
        initialInc
            A Float specifying the initial time increment. The default value is the total time
            period for the step.
        minInc
            A Float specifying the minimum time increment allowed. The default value is the smaller
            of the suggested initial time increment or 10-5 times the total time period.
        maxInc
            A Float specifying the maximum time increment allowed. The default value is the total
            time period for the step.
        matrixSolver
            A SymbolicConstant specifying the type of solver. Possible values are DIRECT and
            ITERATIVE. The default value is DIRECT.
        matrixStorage
            A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC,
            UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT.
        amplitude
            A SymbolicConstant specifying the amplitude variation for loading magnitudes during the
            step. Possible values are STEP and RAMP. The default value is RAMP.
        extrapolation
            A SymbolicConstant specifying the type of extrapolation to use in determining the
            incremental solution for a nonlinear analysis. Possible values are NONE, LINEAR, and
            PARABOLIC. The default value is LINEAR.
        fullyPlastic
            A String specifying the region being monitored for fully Plastic behavior. The default
            value is an empty string.
        noStop
            A Boolean specifying whether to accept the solution to an increment after the maximum
            number of iterations allowed has been completed, even if the equilibrium tolerances are
            not satisfied. The default value is OFF.Warning:You should set **noStop**=ON only in
            special cases when you have a thorough understanding of how to interpret the results.
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same
            name. The default value is False.
        useLongTermSolution
            A Boolean specifying wether to obtain the fully relaxed long-term elastic solution with
            time-domain viscoelasticity or the long-term elastic-Plastic solution for two-layer
            viscoplasticity. The default value is OFF.
        solutionTechnique
            A SymbolicConstant specifying the technique used to for solving nonlinear equations.
            Possible values are FULL_NEWTON and QUASI_NEWTON. The default value is FULL_NEWTON.
        reformKernel
            An Int specifying the number of quasi-Newton iterations allowed before the kernel matrix
            is reformed.. The default value is 8.
        convertSDI
            A SymbolicConstant specifying whether to force a new iteration if severe discontinuities
            occur during an iteration. Possible values are PROPAGATED, CONVERT_SDI_OFF, and
            CONVERT_SDI_ON. The default value is PROPAGATED.
        adaptiveDampingRatio
            A Float specifying the maximum allowable ratio of the stabilization energy to the total
            strain energy and can be used only if **stabilizationMethod** is not NONE. The default
            value is 0.05.
        continueDampingFactors
            A Boolean specifying whether this step will carry over the damping factors from the
            results of the preceding general step. This parameter must be used in conjunction with
            the **adaptiveDampingRatio** parameter. The default value is OFF.

        Returns
        -------
            A StaticStep object.

        Raises
        ------
        RangeError
        """
        super().__init__()
        pass

    def setValues(
        self,
        description: str = "",
        timePeriod: float = 1,
        nlgeom: Boolean = OFF,
        stabilizationMethod: SymbolicConstant = NONE,
        stabilizationMagnitude: float = None,
        adiabatic: Boolean = OFF,
        timeIncrementationMethod: SymbolicConstant = AUTOMATIC,
        maxNumInc: int = 100,
        initialInc: float = None,
        minInc: float = None,
        maxInc: float = None,
        matrixSolver: SymbolicConstant = DIRECT,
        matrixStorage: SymbolicConstant = SOLVER_DEFAULT,
        amplitude: SymbolicConstant = RAMP,
        extrapolation: SymbolicConstant = LINEAR,
        fullyPlastic: str = "",
        noStop: Boolean = OFF,
        useLongTermSolution: Boolean = OFF,
        solutionTechnique: SymbolicConstant = FULL_NEWTON,
        reformKernel: int = 8,
        convertSDI: SymbolicConstant = PROPAGATED,
        adaptiveDampingRatio: float = 0,
        continueDampingFactors: Boolean = OFF,
    ):
        """This method modifies the StaticStep object.

        Parameters
        ----------
        description
            A String specifying a description of the new step. The default value is an empty string.
        timePeriod
            A Float specifying the total time period. The default value is 1.0.
        nlgeom
            A Boolean specifying whether to allow for geometric nonlinearity. The default value is
            OFF.
        stabilizationMethod
            A SymbolicConstant specifying the stabilization type. Possible values are NONE,
            DISSIPATED_ENERGY_FRACTION, and DAMPING_FACTOR. The default value is NONE.
        stabilizationMagnitude
            A Float specifying the damping intensity of the automatic damping algorithm if the
            problem is expected to be unstable, and **stabilizationMethod** is not NONE. The default
            value is 2×10-4.
        adiabatic
            A Boolean specifying whether to perform an adiabatic stress analysis. The default value
            is OFF.
        timeIncrementationMethod
            A SymbolicConstant specifying the time incrementation method to be used. Possible values
            are FIXED and AUTOMATIC. The default value is AUTOMATIC.
        maxNumInc
            An Int specifying the maximum number of increments in a step. The default value is 100.
        initialInc
            A Float specifying the initial time increment. The default value is the total time
            period for the step.
        minInc
            A Float specifying the minimum time increment allowed. The default value is the smaller
            of the suggested initial time increment or 10-5 times the total time period.
        maxInc
            A Float specifying the maximum time increment allowed. The default value is the total
            time period for the step.
        matrixSolver
            A SymbolicConstant specifying the type of solver. Possible values are DIRECT and
            ITERATIVE. The default value is DIRECT.
        matrixStorage
            A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC,
            UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT.
        amplitude
            A SymbolicConstant specifying the amplitude variation for loading magnitudes during the
            step. Possible values are STEP and RAMP. The default value is RAMP.
        extrapolation
            A SymbolicConstant specifying the type of extrapolation to use in determining the
            incremental solution for a nonlinear analysis. Possible values are NONE, LINEAR, and
            PARABOLIC. The default value is LINEAR.
        fullyPlastic
            A String specifying the region being monitored for fully Plastic behavior. The default
            value is an empty string.
        noStop
            A Boolean specifying whether to accept the solution to an increment after the maximum
            number of iterations allowed has been completed, even if the equilibrium tolerances are
            not satisfied. The default value is OFF.Warning:You should set **noStop**=ON only in
            special cases when you have a thorough understanding of how to interpret the results.
        useLongTermSolution
            A Boolean specifying wether to obtain the fully relaxed long-term elastic solution with
            time-domain viscoelasticity or the long-term elastic-Plastic solution for two-layer
            viscoplasticity. The default value is OFF.
        solutionTechnique
            A SymbolicConstant specifying the technique used to for solving nonlinear equations.
            Possible values are FULL_NEWTON and QUASI_NEWTON. The default value is FULL_NEWTON.
        reformKernel
            An Int specifying the number of quasi-Newton iterations allowed before the kernel matrix
            is reformed.. The default value is 8.
        convertSDI
            A SymbolicConstant specifying whether to force a new iteration if severe discontinuities
            occur during an iteration. Possible values are PROPAGATED, CONVERT_SDI_OFF, and
            CONVERT_SDI_ON. The default value is PROPAGATED.
        adaptiveDampingRatio
            A Float specifying the maximum allowable ratio of the stabilization energy to the total
            strain energy and can be used only if **stabilizationMethod** is not NONE. The default
            value is 0.05.
        continueDampingFactors
            A Boolean specifying whether this step will carry over the damping factors from the
            results of the preceding general step. This parameter must be used in conjunction with
            the **adaptiveDampingRatio** parameter. The default value is OFF.

        Raises
        ------
        RangeError
        """
        pass
