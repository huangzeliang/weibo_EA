

{
                        var myChart = echarts.init(document.getElementById("sociality"));
                        var app = {};
                        function setCatData(arr, n, sm) {
                            for (var i = 0; i < arr.length; i++) {
                                listdata.push({
                                    "name": arr[i],
                                    "symbolSize": sm || 10,
                                    "category": n,
                                    "label": {
                                        "normal": {
                                            //   "show": true,
                                            "textStyle": {
                                                "color": colors[n]
                                            }
                                        }
                                    }
                                })
                            }
                        }
                        /**
                        * [setLinkData 设置关键链]
                        * @param {[type]} arr   [description]
                        * @param {[type]} title [description]
                        */
                        function setLinkData(arr, title, cc) {
                            for (var i = 0; i < arr.length; i++) {
                                links.push({
                                    "source": arr[i],
                                    "target": title,
                                    lineStyle: {
                                        normal: {
                                            color: cc
                                        }
                                    }
                                })
                            }
                        }
                        var legendes = ["基本数据", "税收数据", "欠税信息", "行政处罚信息", "重大违法信息", "增值税申报信息", "缴税情况", "税务信用评级", "所得税年度汇算清缴", "企业画像"];
                        var colors = ['#dc44c8', '#6444dc', '#dc4474', '#dc4444', '#68b6ef', '#68efb8', '#ef9b68', '#4c6492', '#4a561a', '#fff'];
                        //   var colors = ['#fff', '#fff', '#fff', '#fff', '#fff', '#fff', '#fff', '#fff', '#fff', '#fff'];
                        //   var colors = ['#72d3f9', '#4185f7', '#62abe1', '#3060ba', '#0057a6', '#00a3d0', '#03a7dc', '#16dcdc', '#2976b2', '#2976b2'];

                        var texts = [];
                        for (var i = 0; i < legendes.length; i++) {
                            texts.push({
                                "name": legendes[i],
                                "itemStyle": {
                                    "normal": {
                                        "color": colors[i],
                                        //   "borderWidth": 30,
                                        //   "shadowBlur": 15,
                                        //   "shadowColor": colors[i],
                                        //   color: '#66ff00',
                                        //   borderColor: 'rgba(255, 255, 255, 0.2)',
                                        //   borderWidth: 6
                                    }
                                }
                            })
                        }
                        var listdata = [];
                        var cat1 = ["基本数据", "企业名称", "社会统一信用代码", "生产经营地址", "纳税人状态", "登记日期", "生产经营地址（共管户国税为准）", "法定代表人", "行业类型", "纳税人类型", "国地最早开业（设立）日期", "登记注册类型（共管户国税为准）", "纳税人登记状态（共管户国税为准）", "增值税最早申报日期", "营业税最早申报日期"];
                        var cat2 = ["税收数据", "所属日期起", "所属日期止", "应税销售收入", "入库税额", "入库税额（消）", "入库税额（营）", "入库税额（企）", "减免税额（增）", "减免税额（消）", "减免税额（营）", "减免税额（企）"];
                        var cat3 = ["欠税信息", "经营地点", "增值税欠税金额", "消费税欠税金额", "所得税欠税金额"];
                        var cat4 = ["行政处罚信息", "案件名称", "行政处罚类别", "行政处罚结果", "行政处罚事由", "行政处罚依据", "处罚金额", "行政处罚日期", "处罚截止日期", "处罚机关", "当前状态"];
                        var cat5 = ["重大违法信息", "中介机构", "从业人员", "案件性质", "主要违法事实", "处罚情况"];
                        var cat6 = ["增值税申报信息", "增值税申报信息-年度", "申报月份", "按适用税率计税销售额", "应补退税额", "按简易办法计税销售额", "免、抵、退办法出口销售额", "免税销售额"];
                        var cat7 = ["缴税情况", "缴税情况-年度", "属期起止", "税种代码", "税款种类", "实缴时间", "实缴税额"];
                        var cat8 = ["税务信用评级", "信用级别", "信用评级年度", "信用评分分数"]
                        var cat9 = ["所得税年度汇算清缴", "所得税年度汇算清缴-年度", "汇算清缴日期", "营业收入", "应纳税所得额", "应纳所得税额"];
                        var cat10 = ["企业"];

                        // 拼装数据
                        setCatData(cat1, 0)
                        setCatData(cat2, 1)
                        setCatData(cat3, 2)
                        setCatData(cat4, 3)
                        setCatData(cat5, 4)
                        setCatData(cat6, 5)
                        setCatData(cat7, 6)
                        setCatData(cat10, 9, 15)
                        var links = [];

                        setLinkData(cat1, "基本数据", colors[0]);
                        setLinkData(cat2, "税收数据", colors[1]);
                        setLinkData(cat3, "欠税信息", colors[2]);
                        setLinkData(cat4, "行政处罚信息", colors[3]);
                        setLinkData(cat5, "重大违法信息", colors[4]);
                        setLinkData(cat6, "增值税申报信息", colors[5]);
                        setLinkData(cat7, "缴税情况", colors[6]);
                        setLinkData(legendes, "企业", colors[9]);

                        //   var planePath = 'path://M1705.06,1318.313v-89.254l-319.9-221.799l0.073-208.063c0.521-84.662-26.629-121.796-63.961-121.491c-37.332-0.305-64.482,36.829-63.961,121.491l0.073,208.063l-319.9,221.799v89.254l330.343-157.288l12.238,241.308l-134.449,92.931l0.531,42.034l175.125-42.917l175.125,42.917l0.531-42.034l-134.449-92.931l12.238-241.308L1705.06,1318.313z';
                        //   var planePath ='path://M30.9,53.2C16.8,53.2,5.3,41.7,5.3,27.6S16.8,2,30.9,2C45,2,56.4,13.5,56.4,27.6S45,53.2,30.9,53.2z M30.9,3.5C17.6,3.5,6.8,14.4,6.8,27.6c0,13.3,10.8,24.1,24.101,24.1C44.2,51.7,55,40.9,55,27.6C54.9,14.4,44.1,3.5,30.9,3.5z M36.9,35.8c0,0.601-0.4,1-0.9,1h-1.3c-0.5,0-0.9-0.399-0.9-1V19.5c0-0.6,0.4-1,0.9-1H36c0.5,0,0.9,0.4,0.9,1V35.8z M27.8,35.8 c0,0.601-0.4,1-0.9,1h-1.3c-0.5,0-0.9-0.399-0.9-1V19.5c0-0.6,0.4-1,0.9-1H27c0.5,0,0.9,0.4,0.9,1L27.8,35.8L27.8,35.8z';
                        var planePath = 'circle';
                        //  var planePath = 'path://M19.300,3.300 L253.300,3.300 C262.136,3.300 269.300,10.463 269.300,19.300 L269.300,21.300 C269.300,30.137 262.136,37.300 253.300,37.300 L19.300,37.300 C10.463,37.300 3.300,30.137 3.300,21.300 L3.300,19.300 C3.300,10.463 10.463,3.300 19.300,3.300 Z';
                        //  var planePath="path://M5,1 2,9 L10,3 1,3 8,9";
                        //  var planePath="path://M25 15 L15 35 L35 35 Z";
                        // console.log(links)
                        // console.log(JSON.stringify(listdata))
                        // console.log(JSON.stringify(texts))
                        // var texts=[{"name":"基本数据","itemStyle":{"normal":{"color":"#dc44c8"}}},{"name":"税收数据","itemStyle":{"normal":{"color":"#6444dc"}}},{"name":"欠税信息","itemStyle":{"normal":{"color":"#dc4474"}}},{"name":"行政处罚信息","itemStyle":{"normal":{"color":"#dc4444"}}},{"name":"重大违法信息","itemStyle":{"normal":{"color":"#68b6ef"}}},{"name":"增值税申报信息","itemStyle":{"normal":{"color":"#68efb8"}}},{"name":"缴税情况","itemStyle":{"normal":{"color":"#ef9b68"}}},{"name":"税务信用评级","itemStyle":{"normal":{"color":"#4c6492"}}},{"name":"所得税年度汇算清缴","itemStyle":{"normal":{"color":"#4a561a"}}}];
                        // var listdata=[{"name":"企业名称","category":0,"label":{"normal":{"show":true,"textStyle":{"color":"#dc44c8"}}}},{"name":"社会统一信用代码","category":0,"label":{"normal":{"show":true,"textStyle":{"color":"#dc44c8"}}}},{"name":"生产经营地址","category":0,"label":{"normal":{"show":true,"textStyle":{"color":"#dc44c8"}}}},{"name":"纳税人状态","category":0,"label":{"normal":{"show":true,"textStyle":{"color":"#dc44c8"}}}},{"name":"登记日期","category":0,"label":{"normal":{"show":true,"textStyle":{"color":"#dc44c8"}}}},{"name":"生产经营地址（共管户国税为准）","category":0,"label":{"normal":{"show":true,"textStyle":{"color":"#dc44c8"}}}},{"name":"法定代表人","category":0,"label":{"normal":{"show":true,"textStyle":{"color":"#dc44c8"}}}},{"name":"行业类型","category":0,"label":{"normal":{"show":true,"textStyle":{"color":"#dc44c8"}}}},{"name":"纳税人类型","category":0,"label":{"normal":{"show":true,"textStyle":{"color":"#dc44c8"}}}},{"name":"国地最早开业（设立）日期","category":0,"label":{"normal":{"show":true,"textStyle":{"color":"#dc44c8"}}}},{"name":"登记注册类型（共管户国税为准）","category":0,"label":{"normal":{"show":true,"textStyle":{"color":"#dc44c8"}}}},{"name":"纳税人登记状态（共管户国税为准）","category":0,"label":{"normal":{"show":true,"textStyle":{"color":"#dc44c8"}}}},{"name":"增值税最早申报日期","category":0,"label":{"normal":{"show":true,"textStyle":{"color":"#dc44c8"}}}},{"name":"营业税最早申报日期","category":0,"label":{"normal":{"show":true,"textStyle":{"color":"#dc44c8"}}}},{"name":"所属日期起","category":1,"label":{"normal":{"show":true,"textStyle":{"color":"#6444dc"}}}},{"name":"所属日期止","category":1,"label":{"normal":{"show":true,"textStyle":{"color":"#6444dc"}}}},{"name":"应税销售收入","category":1,"label":{"normal":{"show":true,"textStyle":{"color":"#6444dc"}}}},{"name":"入库税额","category":1,"label":{"normal":{"show":true,"textStyle":{"color":"#6444dc"}}}},{"name":"入库税额（消）","category":1,"label":{"normal":{"show":true,"textStyle":{"color":"#6444dc"}}}},{"name":"入库税额（营）","category":1,"label":{"normal":{"show":true,"textStyle":{"color":"#6444dc"}}}},{"name":"入库税额（企）","category":1,"label":{"normal":{"show":true,"textStyle":{"color":"#6444dc"}}}},{"name":"减免税额（增）","category":1,"label":{"normal":{"show":true,"textStyle":{"color":"#6444dc"}}}},{"name":"减免税额（消）","category":1,"label":{"normal":{"show":true,"textStyle":{"color":"#6444dc"}}}},{"name":"减免税额（营）","category":1,"label":{"normal":{"show":true,"textStyle":{"color":"#6444dc"}}}},{"name":"减免税额（企）","category":1,"label":{"normal":{"show":true,"textStyle":{"color":"#6444dc"}}}},{"name":"经营地点","category":2,"label":{"normal":{"show":true,"textStyle":{"color":"#dc4474"}}}},{"name":"增值税欠税金额","category":2,"label":{"normal":{"show":true,"textStyle":{"color":"#dc4474"}}}},{"name":"消费税欠税金额","category":2,"label":{"normal":{"show":true,"textStyle":{"color":"#dc4474"}}}},{"name":"所得税欠税金额","category":2,"label":{"normal":{"show":true,"textStyle":{"color":"#dc4474"}}}},{"name":"案件名称","category":3,"label":{"normal":{"show":true,"textStyle":{"color":"#dc4444"}}}},{"name":"行政处罚类别","category":3,"label":{"normal":{"show":true,"textStyle":{"color":"#dc4444"}}}},{"name":"行政处罚结果","category":3,"label":{"normal":{"show":true,"textStyle":{"color":"#dc4444"}}}},{"name":"行政处罚事由","category":3,"label":{"normal":{"show":true,"textStyle":{"color":"#dc4444"}}}},{"name":"行政处罚依据","category":3,"label":{"normal":{"show":true,"textStyle":{"color":"#dc4444"}}}},{"name":"处罚金额","category":3,"label":{"normal":{"show":true,"textStyle":{"color":"#dc4444"}}}},{"name":"行政处罚日期","category":3,"label":{"normal":{"show":true,"textStyle":{"color":"#dc4444"}}}},{"name":"处罚截止日期","category":3,"label":{"normal":{"show":true,"textStyle":{"color":"#dc4444"}}}},{"name":"处罚机关","category":3,"label":{"normal":{"show":true,"textStyle":{"color":"#dc4444"}}}},{"name":"当前状态","category":3,"label":{"normal":{"show":true,"textStyle":{"color":"#dc4444"}}}},{"name":"中介机构","category":4,"label":{"normal":{"show":true,"textStyle":{"color":"#68b6ef"}}}},{"name":"从业人员","category":4,"label":{"normal":{"show":true,"textStyle":{"color":"#68b6ef"}}}},{"name":"案件性质","category":4,"label":{"normal":{"show":true,"textStyle":{"color":"#68b6ef"}}}},{"name":"主要违法事实","category":4,"label":{"normal":{"show":true,"textStyle":{"color":"#68b6ef"}}}},{"name":"处罚情况","category":4,"label":{"normal":{"show":true,"textStyle":{"color":"#68b6ef"}}}},{"name":"年度","category":5,"label":{"normal":{"show":true,"textStyle":{"color":"#68efb8"}}}},{"name":"申报月份","category":5,"label":{"normal":{"show":true,"textStyle":{"color":"#68efb8"}}}},{"name":"按适用税率计税销售额","category":5,"label":{"normal":{"show":true,"textStyle":{"color":"#68efb8"}}}},{"name":"应补退税额","category":5,"label":{"normal":{"show":true,"textStyle":{"color":"#68efb8"}}}},{"name":"按简易办法计税销售额","category":5,"label":{"normal":{"show":true,"textStyle":{"color":"#68efb8"}}}},{"name":"免、抵、退办法出口销售额","category":5,"label":{"normal":{"show":true,"textStyle":{"color":"#68efb8"}}}},{"name":"免税销售额","category":5,"label":{"normal":{"show":true,"textStyle":{"color":"#68efb8"}}}},{"name":"年度","category":6,"label":{"normal":{"show":true,"textStyle":{"color":"#ef9b68"}}}},{"name":"属期起止","category":6,"label":{"normal":{"show":true,"textStyle":{"color":"#ef9b68"}}}},{"name":"税种代码","category":6,"label":{"normal":{"show":true,"textStyle":{"color":"#ef9b68"}}}},{"name":"税款种类","category":6,"label":{"normal":{"show":true,"textStyle":{"color":"#ef9b68"}}}},{"name":"实缴时间","category":6,"label":{"normal":{"show":true,"textStyle":{"color":"#ef9b68"}}}},{"name":"实缴税额","category":6,"label":{"normal":{"show":true,"textStyle":{"color":"#ef9b68"}}}},{"name":"信用级别","category":7,"label":{"normal":{"show":true,"textStyle":{"color":"#4c6492"}}}},{"name":"信用评级年度","category":7,"label":{"normal":{"show":true,"textStyle":{"color":"#4c6492"}}}},{"name":"信用评分分数","category":7,"label":{"normal":{"show":true,"textStyle":{"color":"#4c6492"}}}},{"name":"年度","category":8,"label":{"normal":{"show":true,"textStyle":{"color":"#4a561a"}}}},{"name":"汇算清缴日期","category":8,"label":{"normal":{"show":true,"textStyle":{"color":"#4a561a"}}}},{"name":"营业收入","category":8,"label":{"normal":{"show":true,"textStyle":{"color":"#4a561a"}}}},{"name":"应纳税所得额","category":8,"label":{"normal":{"show":true,"textStyle":{"color":"#4a561a"}}}},{"name":"应纳所得税额","category":8,"label":{"normal":{"show":true,"textStyle":{"color":"#4a561a"}}}}];
                        // var links=[{"source":"Ruff成为企业生态合作伙伴","target":"企业"},{"source":"百度与银联商务正式达成战略合作协议","target":"企业"},{"source":"企业","target":"人脸识别"},{"source":"企业","target":"百度深度学习"},{"source":"企业北京沙龙","target":"企业"},{"source":"2017企业智峰会","target":"企业总经理尹世明云智峰会展示黑科技"},{"source":"企业总经理尹世明云智峰会展示黑科技","target":"企业"},{"source":"企业","target":"图像识别"},{"source":"2017企业智峰会","target":"企业与传媒行业战略合作签约视频时代"},{"source":"企业与传媒行业战略合作签约视频时代","target":"企业"},{"source":"企业","target":"视频封面选图VCS"},{"source":"企业","target":"视频内容分析"},{"source":"企业","target":"语音识别"},{"source":"企业","target":"视频内容审核"},{"source":"企业","target":"理解与交互技术UNIT"},{"source":"企业","target":"视频封面选图"},{"source":"企业","target":"视频内容分析VCA"},{"source":"企业","target":"视频内容审核 VCR"},{"source":"2017企业智峰会","target":"企业高级产品专家黄锋视频AI产品发布"},{"source":"企业高级产品专家黄锋视频AI产品发布","target":"企业"},{"source":"企业","target":"文字识别"},{"source":"2017企业智峰会","target":"华数传媒网络有限公司亮相2017企业智峰会"},{"source":"华数传媒网络有限公司亮相2017企业智峰会","target":"企业"},{"source":"企业","target":"智能推荐BRS"},{"source":"2017企业智峰会","target":"企业ABC技术标识――ABC Inspire发布，进入Cloud2.0时代"},{"source":"企业ABC技术标识――ABC Inspire发布，进入Cloud2.0时代","target":"企业"},{"source":"企业ABC技术标识――ABC Inspire发布，进入Cloud2.0时代","target":"张亚勤"},{"source":"2017企业智峰会","target":"百度公司总裁张亚勤企业智峰会聊云计算"},{"source":"百度公司总裁张亚勤企业智峰会聊云计算","target":"企业"},{"source":"企业","target":"云服务器BBC"},{"source":"百度公司总裁张亚勤企业智峰会聊云计算","target":"张亚勤"},{"source":"未来域，南京度房与企业合作","target":"企业"},{"source":"企业CDN流量包1折闪促","target":"企业"}];
                        var option = {
                            //   backgroundColor: new echarts.graphic.RadialGradient(0.4, 0.4, 0.7, [{
                            //       offset: 0,
                            //       color: '#162436'
                            //   }, {
                            //       offset: 1,
                            //       color: '#000'
                            //   }]),
                            title: {
                                text: '社交关系',
                                left: 'left',
                                top: 450,
                                textStyle: {
                                    color: '#ccc'
                                }
                            },
                            backgroundColor: '#2c343c',
                            legend: {
                                data: legendes,
                                textStyle: {
                                    color: '#fff'
                                },
                                icon: 'circle',
                                type: 'scroll',
                                orient: 'vertical',
                                left: 10,
                                top: 20,
                                bottom: 20,
                                itemWidth: 10,
                                itemHeight: 10

                                // width:5,
                                // height:5,
                                // borderWidth:1,
                                // barBorderRadius:10
                            },
                            tooltip: {
                                formatter: function(parmes) {
                                    if (parmes.data.name) {
                                        return legendes[parmes.data.category] + ">" + parmes.name;
                                    }
                                }
                            },
                            animationDurationUpdate: 300,
                            animationEasingUpdate: 'quinticInOut',
                            series: [{
                                type: 'graph',
                                layout: 'force',
                                symbol: planePath,
                                symbolSize: 5,
                                roam: true,
                                //   focusNodeAdjacency: false,
                                focusNodeAdjacency: true,
                                legendHoverLink: true,
                                draggable: true,
                                force: {
                                    repulsion: 30,
                                    gravity: 0.03,
                                    edgeLength: 50,
                                    layoutAnimation: true
                                },
                                categories: texts,
                                data: listdata,
                                links: links,
                                lineStyle: {
                                    normal: {
                                        opacity: 0.9,
                                        width: 1.5,
                                        curveness: 0
                                    }
                                }
                            }]
                        };
                        myChart.setOption(option);
 }


{
    var dom = document.getElementById("bar");
                    var myChart = echarts.init(dom);
                    var app = {};
                    var option = null;
                    option = {
                        title: {
                                text: '各数据源条数',
                                textStyle: {
                                    color: '#ccc'
                                },
                                // subtext: '虚构数据',
                                left: 'left'
                            },
                        xAxis: {
                            type: 'category',
                            axisLine:{
                                lineStyle:{
                                    color: 'black'
                                }
                            },
                            data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
                        },
                        yAxis: {
                            type: 'value',
                            axisLine:{
                                lineStyle:{
                                    color: 'black'
                                }
                            }
                        },
                        series: [{
                            data: [120, 200, 150, 80, 70, 110, 130],
                            type: 'bar'
                        }]
                    };
                    ;
                    if (option && typeof option === "object") {
                        myChart.setOption(option, true);
                    }
}
{
    
    var dom = document.getElementById("pie");
                        var myChart = echarts.init(dom);
                        var app = {};
                        var option = null;
                        app.title = '各数据源条数比例';

                        option = {
                            title: {
                                text: '各数据源条数比例',
                                textStyle: {
                                    color: '#ccc'
                                },
                                // subtext: '虚构数据',
                                left: 'left'
                            },
                            tooltip: {
                                trigger: 'item',
                                formatter: "{a} <br/>{b}: {c} ({d}%)"
                            },
                            legend: {
                                orient: 'vertical',
                                x: 'left',
                                bottom:20,
                                data:['直达','营销广告','搜索引擎','邮件营销','联盟广告','视频广告','百度','谷歌','必应','其他']
                            },
                            series: [
                                {
                                    name:'访问来源',
                                    type:'pie',
                                    selectedMode: 'single',
                                    radius: [0, '20%'],

                                    label: {
                                        normal: {
                                            position: 'inner'
                                        }
                                    },
                                    labelLine: {
                                        normal: {
                                            show: false
                                        }
                                    },
                                    data:[
                                        {value:335, name:'直达', selected:true},
                                        {value:679, name:'营销广告'},
                                        {value:1548, name:'搜索引擎'}
                                    ]
                                },
                                {
                                    name:'访问来源',
                                    type:'pie',
                                    radius: ['28%', '43%'],
                                    label: {
                                        normal: {
                                            formatter: '{a|{a}}{abg|}\n{hr|}\n  {b|{b}：}{c}  {per|{d}%}  ',
                                            backgroundColor: '#eee',
                                            borderColor: '#aaa',
                                            borderWidth: 1,
                                            borderRadius: 4,
                                            // shadowBlur:3,
                                            // shadowOffsetX: 2,
                                            // shadowOffsetY: 2,
                                            // shadowColor: '#999',
                                            // padding: [0, 7],
                                            rich: {
                                                a: {
                                                    color: '#999',
                                                    lineHeight: 2,
                                                    align: 'center'
                                                },
                                                // abg: {
                                                    // backgroundColor: '#333',
                                                  //  width: '100%',
                                                  //   align: 'right',
                                                  //   height: 22,
                                                 //    borderRadius: [4, 4, 0, 0]
                                              //  },
                                                hr: {
                                                    borderColor: '#aaa',
                                                    width: '100%',
                                                    borderWidth: 0.5,
                                                    height: 0
                                                },
                                                b: {
                                                    fontSize: 16,
                                                    lineHeight: 30
                                                
                                                },
                                                per: {
                                                    color: '#eee',
                                                    backgroundColor: '#334455',
                                                    padding: [2, 4],
                                                    borderRadius: 2
                                                }
                                            }
                                        }
                                    },
                                    data:[
                                        {value:335, name:'直达'},
                                        {value:310, name:'邮件营销'},
                                        {value:234, name:'联盟广告'},
                                        {value:135, name:'视频广告'},
                                        {value:1048, name:'百度'},
                                        {value:251, name:'谷歌'},
                                        {value:147, name:'必应'},
                                        {value:102, name:'其他'}
                                    ]
                                }
                            ]
                        };;
                        if (option && typeof option === "object") {
                            myChart.setOption(option, true);
                        }
}
