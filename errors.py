from string_with_Arrows import string_with_arrows

class Error:
    def __init__(self, pos_st, pos_end , error_name, details):
        self.pos_st = pos_st
        self.pos_end = pos_end
        self.error_name = error_name
        self.details = details

    def as_string(self):
        result = f"{self.error_name} : {self.details}"
        context = f"File - {self.pos_st.file_name}, Line - {self.pos_st.line}"
        result +='\n\n' + string_with_arrows(self.pos_st.file_text, self.pos_st, self.pos_end)
        return f"{result}\n{context}"

class IllegalCharError(Error):
    def __init__(self, pos_st, post_end, details):
        self.details = details
        self.pos_st = pos_st
        self.pos_end = post_end
        super().__init__(self.pos_st, self.pos_end, 'Only the wise mayst speak in ThyLang. This character is treason!', self.details)


class InvalidSyntaxError(Error):
    def __init__(self, pos_st, post_end, details):
        self.details = details
        self.pos_st = pos_st
        self.pos_end = post_end
        super().__init__(self.pos_st, self.pos_end, 'Hark! Thy script hath faltered in syntax’s sacred halls!', self.details)

class ExpectedCharError(Error):
    def __init__(self, pos_st, post_end, details):
        self.details = details
        self.pos_st = pos_st
        self.pos_end = post_end
        super().__init__(self.pos_st, self.pos_end, 'How darest thou omit a character?!', self.details)




class RunTimeError(Error):
    def __init__(self, pos_st, post_end, details, context):
        self.context = context
        self.details = details
        self.pos_st = pos_st
        self.pos_end = post_end
        super().__init__(self.pos_st, self.pos_end, '"Mid-spell, a tear in reality hath unraveled all!', self.details)

    def generate_traceback(self):
        result = ' '
        pos = self.pos_st
        ctx = self.context

        while ctx:
            result = f'  File {pos.file_name}, line {str(pos.line + 1)}, in {ctx.display_name}\n' + result
            pos = ctx.parent_entry_pos
            ctx = ctx.parent

        return 'Traceback (most recent call last):\n' + result

    def as_string(self):
        result = self.generate_traceback()
        result = f"{self.error_name} : {self.details}"
        result += '\n\n' + string_with_arrows(self.pos_st.file_text, self.pos_st, self.pos_end)
        return result