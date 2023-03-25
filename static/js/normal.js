
window.onload = function(){
// login page start
    var _rstrsBtn = document.getElementById("button"),			//獲取過濾按鈕物件
            _strs1 = document.getElementById("username"),			//獲取被過濾元素
            _strs2 = document.getElementById("password");			//獲取被過濾元素

    document.getElementById("username").setAttribute("autocomplete", "off");//設定內容
    document.getElementById("password").setAttribute("autocomplete", "off");//設定內容

    _strs1.oncopy = function(){		//禁止複製事件
        return false;
    }
    _strs1.onpaste = function(){		//禁止貼上
        return false;
    }
    _strs2.oncopy = function(){		//禁止複製事件
        return false;
    }
    _strs2.onpaste = function(){		//禁止貼上
        return false;
    }

    if(_strs2) {					//判斷是否存在banInputMethod
        var clearChinese = function(_this){
            var _v = _this.value;
            _this.value = _v.replace(/[\u4e00-\u9fa5]/g,"");	//正則替換中文字元
        }
        _strs2.onkeyup = function(){				//keyup事件
            clearChinese(this);
        }
        _strs2.onblur = function(){				//blur事件
            clearChinese(this);
        }
    }

    _rstrsBtn.onclick = function(){//去除空格
        _strs1.value = _strs1.value.replace( /^(\s|\u00A0)+|(\s|\u00A0)+$/g, "" );//正規表示式替換
        _strs2.value = _strs2.value.replace( /^(\s|\u00A0)+|(\s|\u00A0)+$/g, "" );//正規表示式替換
        if(!_strs1.value.replace( /^(\s|\u00A0)+|(\s|\u00A0)+$/g, "" ) | !_strs2.value.replace( /^(\s|\u00A0)+|(\s|\u00A0)+$/g, "" )){
            alert("您的輸入為空！");
        }
    }
// login page end

// create page start
    //密碼強度驗證開始
    function setCss(_this, cssOption){//設定樣式
        if ( !_this || _this.nodeType === 3 || _this.nodeType === 8 || !_this.style ) {
            return;
        }
        for(var cs in cssOption){
            _this.style[cs] = cssOption[cs];
        }
        return _this;
    }

    function trim(chars){//去除字串左右兩邊的空格
        return (chars || "").replace(/^(\s|\u00A0)+|(\s|\u00A0)+$/g, "" );
    }

    function password(password, showStrength){
        var self = this;
        /*字元權重：
        數位1，字母2 ，其他字元為3
        當密碼長度小於6為不符合標準，
        長度大=6強度小於10，強度弱，
        長度大=6 強度>=10 <15，強度中，
        長度大=6 強度>=15 強*/
        password.onkeyup = function(){
            var _color = ["red", "blue", "orange", "green"],
                    msgs = ["密碼太短","弱","中","強"],
                    _strength= 0,
                    _v = trim(password.value)
            _vL = _v.length,
                    i = 0;

            var charStrength = function(char){//計算單個字元強度
                if (char>=48 && char <=57){ //數字
                    return 1;
                }
                if (char>=97 && char <=122) {//小寫
                    return 2;
                }else{
                    return 3; //特殊字元
                }
            }

            if(_vL < 6){//計算模式
                showStrength.innerText = msgs[0];
                setCss(showStrength, {
                    "color":_color[0]
                })
            }else{
                for( ; i < _vL ; i++){
                    _strength+=charStrength(_v.toLocaleLowerCase().charCodeAt(i));
                }
                if(_strength < 10){
                    showStrength.innerText = msgs[1];
                    setCss(showStrength, {
                        "color":_color[1]
                    })
                }
                if(_strength >= 10 && _strength < 15){
                    showStrength.innerText = msgs[2];
                    setCss(showStrength, {
                        "color":_color[2]
                    })
                }
                if(_strength >= 15){
                    showStrength.innerText = msgs[3];
                    setCss(showStrength, {
                        "color":_color[3]
                    })
                }
            }
        }
    }
    password(
            document.getElementById("password"),
            document.getElementById("showStrength"));
    //密碼強度驗證結束

    //常見的驗證規則開始
    var getRegular = function(rstr){
        var regData={};//正則資料儲存欄位
        regData.rtrim = /^(\s|\u00A0)+|(\s|\u00A0)+$/g;// 去除空格的正則
        regData.Chinese = /[\u4e00-\u9fa5]/g;//中文
        regData.nonumber = /\D/g;//數字
        regData.nochinese = /[^\u4e00-\u9fa5]/g;//非中文
        regData.email = /^\s*[a-zA-Z0-9]+(([\._\-]?)[a-zA-Z0-9]+)*@[a-zA-Z0-9]+([_\-][a-zA-Z0-9]+)*(\.[a-zA-Z0-9]+([_\-][a-zA-Z0-9]+)*)+\s*$/;//郵件
        regData.phone = /^\(?(\d{2})\)?[\s\-]?(\d{4})\-?(\d{4})$/;//電話
        regData.decimalNumber = /^\d+(\.\d+)+$/;//帶小數位的數字
        regData.htmlTags = /<[\/\!]*[^<>]*>/ig;//html

        return regData[rstr];

    },
    forElementArr = function(_elementArr, callBack){
        var arr =_elementArr,
                self = this
                ;

        if(!(_elementArr instanceof Array)) {
            arr = [_elementArr];
        };
        for(var i= 0,arrLen = arr.length ;i<arrLen;i++){
            var arrI = arr[i];
            if(typeof arrI == "string"){
                arrI = self.getElement(arrI);
            }
            callBack && callBack(i, arrI);
        }
    },
    verification = function(str, reg){
        return getRegular(reg).test(str);
    },
    setCss = function(_this, cssOption){
        if ( !_this || _this.nodeType === 3 || _this.nodeType === 8 || !_this.style ) {
            return;
        }
        for(var cs in cssOption){
            _this.style[cs] = cssOption[cs];
        }
        return _this;
    };

    forElementArr([
        document.getElementById("e-mail")
    ], function(index, _this){

        _this.onkeyup = function(){
            var _v = this.value.replace( /^(\s|\u00A0)+|(\s|\u00A0)+$/g, "" ),//獲取被處理的元素值
                    _reg = this.getAttribute("data-reg"),//獲取正規表示式
                    __reg = _reg.indexOf(",") > 0 ? _reg.split(","): [_reg],//如果含有“,”則將其轉換成多陣列
                    _regLen = __reg.length,//陣列長度
                    _emsg = this.getAttribute("data-emsg"),//錯誤資訊顯示
                    _smsg = this.getAttribute("data-smsg"),//通過資訊顯示
                    _target = document.getElementById(this.getAttribute("data-tmsg")),//獲取顯示資訊的元素
                    i = 0;
            for(; i < _regLen ; i++){
                if(!verification(_v, __reg[i])){
                    _target.innerHTML = _emsg ;
                    setCss(_target, {
                        "color":"red"
                    })
                    return;
                }
            }
            _target.innerHTML = _smsg ;
            setCss(_target, {
                "color":"green"
            })
        }
    });
    //常見的驗證規則結束
// create page end

};

