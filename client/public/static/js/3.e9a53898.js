(window.webpackJsonp=window.webpackJsonp||[]).push([[3],{283:function(e,t,s){"use strict";s.r(t);s(89);var l,a=s(17),n=s(38),i=s(51),r={name:"ModuleSelect",data:function(){return{result:["",""]}},computed:Object(n.a)({},Object(i.c)("binary/modules",["modules","loading"]),{selected:function(){return""!==this.result[0]&&""!==this.result[1]}}),watch:{result:{deep:!0,handler:function(){this.emitResult()}}},created:function(){this.emitResult()},methods:{emitResult:function(){this.selected?this.$emit("input",this.result):this.$emit("input",null)}}},u=s(19),c={name:"AnalysisApi",components:{ModuleSelect:Object(u.a)(r,function(){var e=this,t=e.$createElement,s=e._self._c||t;return s("ElForm",[s("ElFormItem",{attrs:{label:e.$t("binary.modules.select.module_1")}},[s("ElSelect",{attrs:{clearable:"",loading:e.loading,placeholder:e.$t("binary.modules.select.module_1_placeholder")},model:{value:e.result[0],callback:function(t){e.$set(e.result,0,t)},expression:"result[0]"}},[e._l(e.modules,function(t){return[t.id!=e.result[1]?s("ElOption",{key:t.id,attrs:{label:"["+t.id+"] "+t.name,value:t.id}}):e._e()]})],2)],1),e._v(" "),s("ElFormItem",{attrs:{label:e.$t("binary.modules.select.module_2")}},[s("ElSelect",{attrs:{clearable:"",loading:e.loading,placeholder:e.$t("binary.modules.select.module_2_placeholder")},model:{value:e.result[1],callback:function(t){e.$set(e.result,1,t)},expression:"result[1]"}},[e._l(e.modules,function(t){return[t.id!=e.result[0]?s("ElOption",{key:t.id,attrs:{label:"["+t.id+"] "+t.name,value:t.id}}):e._e()]})],2)],1)],1)},[],!1,null,null,null).exports},data:function(){return{selectedModules:null,k:2,matchAlgorithm:"km",executing:!1}},computed:{buttonText:function(){return this.analysing?this.$t("status.analysing"):this.$t("buttons.submit")},buttonDisabled:function(){return!this.selectedModules||this.executing}},methods:{startAnalysis:(l=Object(a.a)(regeneratorRuntime.mark(function e(){var t;return regeneratorRuntime.wrap(function(e){for(;;)switch(e.prev=e.next){case 0:if(!this.buttonDisabled){e.next=2;break}return e.abrupt("return");case 2:return e.prev=2,this.executing=!0,e.next=6,this.$axios.post(this.$api.binary.analysis.api(),{module_1:this.selectedModules[0],module_2:this.selectedModules[1],k:this.k,algorithm:this.matchAlgorithm});case 6:t=e.sent,e.t0=t.data.err,e.next=1===e.t0?10:2===e.t0?12:14;break;case 10:return this.$message.warning(this.$t("binary.analysis.messages.pending")),e.abrupt("break",15);case 12:return this.$message.success(this.$t("binary.analysis.messages.start")),e.abrupt("break",15);case 14:this.$message.success(this.$t("binary.analysis.messages.done"));case 15:e.next=20;break;case 17:e.prev=17,e.t1=e.catch(2),this.$message.error(this.$t("binary.analysis.messages.error"));case 20:return e.prev=20,this.executing=!1,e.finish(20);case 23:case"end":return e.stop()}},e,this,[[2,17,20,23]])})),function(){return l.apply(this,arguments)})}},o=Object(u.a)(c,function(){var e=this,t=e.$createElement,s=e._self._c||t;return s("div",{directives:[{name:"loading",rawName:"v-loading.fullscreen.lock",value:e.executing,expression:"executing",modifiers:{fullscreen:!0,lock:!0}}],attrs:{"element-loading-text":e.$t("status.executing")}},[s("PageTitle",[e._v(e._s(e.$t("binary.analysis.api.title")))]),e._v(" "),s("ModuleSelect",{model:{value:e.selectedModules,callback:function(t){e.selectedModules=t},expression:"selectedModules"}}),e._v(" "),s("p",{staticClass:"hint"},[e._v(e._s(e.$t("binary.analysis.api.select_modules_hint")))]),e._v(" "),s("hr"),e._v(" "),s("ElForm",[s("ElFormItem",{attrs:{label:e.$t("binary.analysis.api.call_depth")}},[s("ElInputNumber",{attrs:{min:0,max:10},model:{value:e.k,callback:function(t){e.k=t},expression:"k"}})],1),e._v(" "),s("p",{staticClass:"hint"},[e._v(e._s(e.$t("binary.analysis.api.call_depth_hint")))]),e._v(" "),s("ElFormItem",{attrs:{label:e.$t("binary.analysis.api.match_algorithm")}},[s("ElSelect",{model:{value:e.matchAlgorithm,callback:function(t){e.matchAlgorithm=t},expression:"matchAlgorithm"}},[s("ElOption",{attrs:{label:"KM",value:"km"}})],1)],1),e._v(" "),s("p",{staticClass:"hint"},[e._v(e._s(e.$t("binary.analysis.api.match_algorithm_hint")))])],1),e._v(" "),s("hr"),e._v(" "),s("ElButton",{attrs:{type:"primary",disabled:!e.selectedModules},on:{click:e.startAnalysis}},[e._v("\n    "+e._s(e.buttonText)+"\n  ")])],1)},[],!1,null,null,null);t.default=o.exports}}]);