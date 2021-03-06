from pywps import Process, LiteralInput
from pywps.app.Common import Metadata
from pywps.ext_autodoc import MetadataUrl
from pywps.app.exceptions import ProcessError

import logging
LOGGER = logging.getLogger("PYWPS")


class ShowError(Process):
    """Show a user friendly error message using :class:`ProcessError`.

    An example request::

        http://localhost:5000/wps?
            version=1.0.0&
            service=wps&
            request=Execute&
            identifier=show_error&
            DataInputs=message=bad-day;nice=true
    """
    def __init__(self):
        inputs = [
            LiteralInput('message', 'Error Message', data_type='string',
                         abstract='Enter an error message that will be returned.',
                         default="This process failed intentionally.",
                         min_occurs=1,),
            LiteralInput('nice', 'Be nice and show a friendly error message. Default: true',
                         data_type='boolean',
                         default=True, ),
        ]

        super(ShowError, self).__init__(
            self._handler,
            identifier='show_error',
            title='Show a WPS Error',
            abstract='This process will fail intentionally with a friendly WPS error message.',
            metadata=[
                Metadata('PyWPS', 'https://pywps.org/'),
                Metadata('Birdhouse', 'http://bird-house.github.io/'),
                MetadataUrl('User Guide',
                            'http://emu.readthedocs.io/en/latest/',
                            anonymous=True),
            ],
            version='1.0',
            inputs=inputs,
            # outputs=outputs,
            store_supported=True,
            status_supported=True
        )

    @staticmethod
    def _handler(request, response):
        response.update_status('PyWPS Process started.', 0)

        LOGGER.info("wps_error started ...")
        if request.inputs['nice'][0].data is True:
            raise ProcessError(request.inputs['message'][0].data)
        else:
            raise Exception("Sorry, we have no explanation for this error.")
