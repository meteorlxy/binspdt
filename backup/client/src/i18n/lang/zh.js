import zhElement from 'element-ui/lib/locale/lang/zh-CN'

const zh = {
  ...zhElement,
  buttons: {
    submit: '提交',
    refresh: '刷新',
    remove: '移除'
  },
  status: {
    loading: '加载中...',
    importing: '导入中...',
    analysing: '分析中...'
  },
  messages: {
    title: {
      warning: '注意'
    }
  },
  routes: {
    home: '主页',
    binary: '目标代码',
    source: '源代码',
    modules: '模块',
    analysis: '分析',
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
        get_error: '加载模块时发生错误 ({msg})',
        import_success: '模块导入成功',
        import_error: '导入模块时发生错误 ({msg})',
        remove_confirm: '确认要删除该模块{name}吗？',
        remove_success: '模块删除成功',
        remove_error: '移除模块时发生错误 ({msg})'
      }
    },
    analysis: {
      api: {
        call_depth: '调用深度',
        select_modules_hint: '选择两个模块，计算它们的API相似性',
        call_depth_hint: '设定API Birthmarking的调用深度(k) [默认值 2]',
        messages: {
          analyse_success: 'API相似性分析成功',
          analyse_error: '计算API相似性时发生错误({msg})'
        },
        result: {
          title: '分析结果'
        }
      }
    }
  }
}

export default zh
