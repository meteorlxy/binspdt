import enElement from 'element-ui/lib/locale/lang/en'

const en = {
  ...enElement,
  buttons: {
    submit: 'Submit',
    refresh: 'Refresh',
    remove: 'Remove'
  },
  status: {
    loading: 'Loading...',
    importing: 'Importing...',
    analysing: 'Analysing...'
  },
  messages: {
    title: {
      warning: 'Warning'
    }
  },
  routes: {
    home: 'Home',
    modules: 'Modules',
    binary: 'Binary Code',
    source: 'Source Code',
    analysis: 'Analysis',
    api: 'API',
    basic_block: 'Basic Block'
  },
  home: {
    welcome: 'Welcome to BINSPDT',
    fullname: 'BINary Software Plagiarism Detection Tool',
    lang: 'Language'
  },
  binary: {
    modules: {
      import_button: 'Import idb File',
      table: {
        id: 'ID',
        name: 'Name',
        architecture: 'Architecture',
        import_time: 'Import Time',
        exporter: 'Exporter',
        base_address: 'Base Address',
        md5: 'MD5',
        sha1: 'SHA1',
        operation: 'Operation'
      },
      select: {
        module_1: 'Module 1',
        module_2: 'Module 2',
        module_1_placeholder: 'Please select module 1',
        module_2_placeholder: 'Please select module 2'
      },
      messages: {
        get_success: 'Module loaded successfully',
        get_error: 'Error occurs when loading modules ({msg})',
        import_success: 'Module imported successfully',
        import_error: 'Error occurs when importing module ({msg})',
        remove_confirm: 'Confirm to remove module {name} ?',
        remove_success: 'Module removed successfully',
        remove_error: 'Error occurs when removing module ({msg})'
      }
    },
    analysis: {
      api: {
        call_depth: 'Call Depth',
        select_modules_hint: 'Choose two modules to calculate their API similarity',
        call_depth_hint: 'Set the call depth (k) of API birthmarking. [default 2]',
        messages: {
          analyse_success: 'API similarity analysed successfully',
          analyse_error: 'Error occurs when analysing API similarity ({msg})'
        },
        result: {
          title: 'Analysis Result',
          function_num: 'Number of Functions'
        }
      }
    }
  }
}

export default en
