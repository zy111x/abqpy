from .Profile import Profile


class IProfile(Profile):
    """The IProfile object defines the properties of an I profile.
    The IProfile object is derived from the Profile object.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import section
        mdb.models[name].profiles[name]
        import odbSection
        session.odbs[name].profiles[name]

    The corresponding analysis keywords are:

    - BEAM SECTION
    """

    def __init__(
        self,
        name: str,
        l: float,
        h: float,
        b1: float,
        b2: float,
        t1: float,
        t2: float,
        t3: float,
    ):
        """This method creates an IProfile object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].IProfile
            session.odbs[name].IProfile

        Parameters
        ----------
        name
            A String specifying the repository key.
        l
            A Float specifying the **l** dimension (offset of 1-axis from the bottom flange surface)
            of the I profile. For more information, see [Beam cross-section
            library](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEELMRefMap/simaelm-c-beamcrosssectlib.htm?ContextScope=all).
        h
            A Float specifying the **h** dimension (height) of the I profile.
        b1
            A Float specifying the **b1** dimension (bottom flange width) of the I profile.
        b2
            A Float specifying the **b2** dimension (top flange width) of the I profile.
        t1
            A Float specifying the **t1** dimension (bottom flange thickness) of the I profile.
        t2
            A Float specifying the **t2** dimension (top flange thickness) of the I profile.
        t3
            A Float specifying the **t3** dimension (web thickness) of the I profile.

        Returns
        -------
            An IProfile object.

        Raises
        ------
        RangeError

        """
        super().__init__()
        pass

    def setValues(self):
        """This method modifies the IProfile object.

        Raises
        ------
        RangeError

        """
        pass
