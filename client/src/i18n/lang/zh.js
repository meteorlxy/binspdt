import zhElement from 'element-ui/lib/locale/lang/zh-CN'

const zh = {
  ...zhElement,
  buttons: {
    submit: '提交',
    refresh: '刷新',
    remove: '移除',
    details: '详情'
  },
  status: {
    loading: '加载中...',
    importing: '导入中...',
    analysing: '分析中...',
    executing: '处理中...'
  },
  messages: {
    title: {
      info: '消息',
      success: '成功',
      warning: '警告',
      error: '错误'
    }
  },
  routes: {
    home: '主页',
    binary: '目标代码',
    source: '源代码',
    modules: '模块',
    analysis: '分析',
    results: '分析结果',
    api: 'API',
    basic_block: '基本块'
  },
  home: {
    welcome: '欢迎使用BINSPDT',
    fullname: 'BINary Software Plagiarism Detection Tool',
    lang: '语言'
  },
  binary: {
    modules: {
      title: '二进制文件模块',
      import_button: '导入idb文件',
      table: {
        id: 'ID',
        name: '模块名称',
        architecture: '架构',
        import_time: '导入时间',
        exporter: '导出工具',
        base_address: '起始地址',
        md5: 'MD5',
        sha1: 'SHA1',
        functions_count: '函数数量',
        basic_blocks_count: '基本块数量',
        instructions_count: '指令数量',
        operation: '操作'
      },
      select: {
        module_1: '模块1',
        module_2: '模块2',
        module_1_placeholder: '请选择模块1',
        module_2_placeholder: '请选择模块2'
      },
      messages: {
        get_success: '模块加载成功',
        get_error: '加载模块时发生错误',
        import_success: '模块导入成功',
        import_error: '导入模块时发生错误',
        remove_confirm: '确认要删除该模块{name}吗？',
        remove_success: '移除模块{name}成功',
        remove_error: '移除模块{name}失败',
        details_success: '读取模块{name}详情成功',
        details_error: '读取模块{name}详情失败'
      }
    },
    analysis: {
      api: {
        title: 'API相似性分析',
        select_modules_hint: '选择两个模块，计算它们的API相似性',
        call_depth: '调用深度[k]',
        call_depth_hint: '设定API Birthmarking的调用深度(k) [默认值 2]',
        match_algorithm: '匹配算法',
        match_algorithm_hint: '设定相似函数的整体匹配算法 [默认值 KM]',
        result: {
          overall_similarity: '整体相似度',
          function_num: '函数/方法数量'
        }
      },
      messages: {
        start: '分析已开始',
        pending: '分析正在进行中...',
        done: '分析已完成，前往[结果]面板查看分析结果',
        error: '启动分析时发生错误'
      }
    },
    results: {
      title: '相似性分析结果',
      table: {
        id: 'ID',
        type: '类型',
        module_1: '模块 1',
        module_2: '模块 2',
        status: '状态',
        created_at: '创建时间',
        finished_at: '完成时间',
        operation: '操作'
      },
      status: {
        pending: '分析中',
        done: '已完成'
      },
      messages: {
        get_success: '获取分析结果列表成功',
        get_error: '获取分析结果列表失败',
        details_success: '获取分析结果{name}详情成功',
        details_error: '获取分析结果{name}详情失败'
      }
    }
  }
}

export default zh
