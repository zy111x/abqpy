from abaqusConstants import *
from .StdStabilization import StdStabilization
from ..Model.ModelBase import ModelBase


class InteractionContactStabilizationModel(ModelBase):

    def StdStabilization(
        self,
        name: str,
        zeroDistance: float = None,
        reductionFactor: float = 0,
        scaleFactor: float = 1,
        tangentialFactor: float = 0,
        amplitude: str = "",
        reset: Boolean = OFF,
    ) -> StdStabilization:
        """This method creates a StdStabilization object.

        .. note::
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].StdStabilization

        Parameters
        ----------
        name
            A String specifying the contact stabilization repository key.
        zeroDistance
            None or a Float specifying the clearance distance at which the stabilization becomes
            zero. The default value is None.
        reductionFactor
            A Float specifying the factor by which the analysis will reduce the contact
            stabilization coefficient per increment. The default value is 0.1.
        scaleFactor
            A Float specifying the factor by which the analysis will scale the contact stabilization
            coefficient. The default value is 1.0.
        tangentialFactor
            A Float specifying the factor that scales the contact stabilization coefficient in the
            tangential direction. The default value is 0.0.
        amplitude
            A String specifying the name of the Amplitude object that defines a time-dependent scale
            factor for contact stabilization over the step. The default value is an empty string.
        reset
            A Boolean specifying whether to cancel carryover effects from contact stabilization
            specifications involving nondefault amplitudes that appeared in previous steps. The
            default value is OFF.

        Returns
        -------
        StdStabilization
            A :py:class:`~abaqus.Interaction.StdStabilization.StdStabilization` object.

        Raises
        ------
        RangeError
        """
        self.contactStabilizations[name] = interaction = StdStabilization(
            name,
            zeroDistance,
            reductionFactor,
            scaleFactor,
            tangentialFactor,
            amplitude,
            reset,
        )
        return interaction