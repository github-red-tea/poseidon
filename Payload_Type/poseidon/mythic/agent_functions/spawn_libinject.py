from mythic_payloadtype_container.MythicCommandBase import *
import json

class SpawnLibinjectArguments(TaskArguments):
    def __init__(self, command_line):
        super().__init__(command_line)
        self.args = {
            "application" : CommandParamter(
                name="application",
                type=ParamterType.String,
                required=True,
                description="Path to the target application/binary"
            ),
            "dylibpath": CommandParameter(
                name="dylibpath",
                type=ParamterType.String,
                required=True,
                description="Path to the dylib on disk that will be injected into the target application"
            ),
            "arguments": CommandParameter(
                name="arguments",
                type=ParameterType.String,
                required=False,
                description="Command line arguments for the target application/binary"
            ),
            "hideApp": CommandParameter(
                name="hideApp",
                type=ParameterType.Boolean,
                required=True,
                description="If true, launch the application with the kLSLaunchAndHide flag set. If false, use the kLSLaunchDefaults flag"
            )
        }

    async def parse_arguments(self):
        if len(self.command_line) > 0:
            if self.command_line[0] == "{":
                self.load_args_from_json_string(self.command_line)
            else:
                raise ValueError("Missing JSON arguments")

        else:
            raise ValueError("Missing arguments")
    
class SpawnLibinjectCommand(CommandBase):
    cmd = "spawnlibinject"
    needs_admin = False
    help_cmd = "spawnlibinject"
    description = "Spawn an application/binary and inject a dylib with the DYLD_INSERT_LIBRARIES environment variable"
    version = 1
    author = "@xorrior @_r3ggi"
    attackmapping = ["T1574.006"]
    argument_class = SpawnLibinjectArguments
    attributes = CommandAttributes(
        supported_os=[SupportedOS.MacOS]
    )

    async def create_tasking(self, task: MythicTask) -> MythicTask:
        return task

    async def process_response(self, response: AgentResponse):
        pass
