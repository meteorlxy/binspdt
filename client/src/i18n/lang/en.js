const en = {
  buttons: {
    submit: 'Submit',
    refresh: 'Refresh',
    remove: 'Remove',
    details: 'Details'
  },
  status: {
    loading: 'Loading...',
    importing: 'Importing...',
    analysing: 'Analysing...',
    executing: 'Executing...',
    error: 'Error'
  },
  messages: {
    title: {
      info: 'Info',
      success: 'Success',
      warning: 'Warning',
      error: 'Error'
    }
  },
  routes: {
    home: 'Home',
    modules: 'Modules',
    binary: 'Binary Code',
    source: 'Source Code',
    analysis: 'Analysis',
    results: 'Analysis Results',
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
      title: 'Binary Modules',
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
        functions_count: 'Functions Count',
        basic_blocks_count: 'Basic Blocks Count',
        instructions_count: 'Instructions Count',
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
        get_error: 'Error occurs when loading modules',
        import_success: 'Module imported successfully',
        import_error: 'Error occurs when importing module',
        remove_confirm: 'Confirm to remove module {name} ?',
        remove_success: 'Removed module {name}',
        remove_error: 'Removeing module {name}',
        details_success: 'Loaded details of module {name}',
        details_error: 'Loading details of module {name}'
      }
    },
    analysis: {
      api: {
        title: 'API Similarity Analysis',
        select_modules_hint: 'Choose two modules to calculate their API similarity',
        call_depth: 'Call Depth [k]',
        call_depth_hint: 'Set the call depth (k) of API birthmarking [default 2]',
        match_algorithm: 'Match Algorithm',
        match_algorithm_hint: 'Set the algorithm for matching similar functions [default KM]',
        result: {
          overall_similarity: 'Overall Similarity',
          functions_with_api_count: 'Number of Functions with API calls in k call depth',
          similar_functions: 'Similar Functions',
          function_api: 'API calls of Function in Module [{module}]'
        }
      },
      messages: {
        start: 'Analysis started.',
        pending: 'Analysis is in progress...',
        done: 'Analysis finished. Go to the [Result] panel to check the result.',
        error: 'Error occurs when starting analysis.'
      }
    },
    results: {
      title: 'Results of Similarity Analysis',
      table: {
        id: 'ID',
        type: 'Type',
        module_1: 'Module 1',
        module_2: 'Module 2',
        status: 'Status',
        created_at: 'Create Time',
        finished_at: 'Finish Time',
        operation: 'Operation'
      },
      status: {
        pending: 'Analysing',
        done: 'Finished'
      },
      messages: {
        get_success: 'Loaded list of analysis results',
        get_error: 'Loading list of analysis results',
        details_success: 'Loaded details of result {name}',
        details_error: 'Loading details of result {name}',
        close_confirm: 'Confirm to close? (Remember to save it)'
      },
      result: {
        title: 'Analysis Result',
        save: 'Save',
        close: 'Close',
        similarity: 'Similarity',
        module_details: 'Module {name} Details',
        module_function_address: 'Function Address of Module {name}'
      }
    }
  }
}

export default en
