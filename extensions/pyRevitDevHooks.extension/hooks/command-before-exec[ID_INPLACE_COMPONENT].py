# pylint: skip-file
import hooks_logger as hl
hl.log_hook(__file__,
    {
        "cancellable?": str(__eventargs__.Cancellable),
        "command_id": str(__eventargs__.CommandId.Name),
        "doc_title": str(__eventargs__.ActiveDocument.Title),
        "using_cmddata": str(__eventargs__.UsingCommandData),
    }
)