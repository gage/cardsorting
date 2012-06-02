function S4() {
   return (((1+Math.random())*0x10000)|0).toString(16).substring(1);
}
function guid() {
   return (S4()+S4()+"-"+S4()+"-"+S4()+"-"+S4()+"-"+S4()+S4()+S4());
}

if(typeof String.prototype.trim !== 'function') {
    String.prototype.trim = function() {
      return this.replace(/^\s+|\s+$/g, '');
    }
}

var WfView = Backbone.View.extend({
    
    //backbone functions 
    initialize: function(options){
        _.bindAll(this, 'positionItems', 'addItem');
        //this.feedTemplateCompiled = _.template($("#template_wall_feed").html());
        this.colWidth = 200;
        this.colGap = 10;
        this.rowGap = 10;
        this.colHeightArray = new Array();
        
        $('.wfItem', this.el).css('position', 'absolute');
        $('.wfItem', this.el).css('width', this.colWidth);
        
        window.onresize = $.proxy(function(event) {
            this.positionItems();   
        },this);
        this.positionItems();
    },
    
    positionItems: function(){
        var containerWidth = this.$el.width();
        var numOfCol = Math.floor((containerWidth - this.colGap)/(this.colWidth + this.colGap));
        this.colHeightArray = [];
        for(var i=0; i < numOfCol; i++){
            this.colHeightArray.push(0);
        };
        var _this = this;
        $('.wfItem', this.el).each(function(){
            var minColHeight = _.min(_this.colHeightArray)
            var minColInd = _.indexOf(_this.colHeightArray, minColHeight);
            var top = minColHeight;
            var left = (minColInd + 1)*_this.colGap + minColInd*_this.colWidth;
            $(this).css('top', top);
            $(this).css('left', left);
            
            _this.colHeightArray[minColInd] += $(this).height() + _this.rowGap;
            
        });
        $('.wfItemWrapper', this.el).height(_.max(this.colHeightArray));
        $('.wfItemWrapper', this.el).width(containerWidth);
        //this.$el.height(_.max(this.colHeightArray));
        
    }, 
    
    addItem: function(){
        //TODO: ADD ITEM FUNCTION
        
    }
    
    
    
});

var Utils = Utils || {};
Utils.Lightbox = Utils.Lightbox || {};


/*
 * a global object to keep track of all lightboxes
 */
var lightboxGlobal = Backbone.Model.extend({
    defaults: {
        'count': 0,
        'divId': 'lightBox_',
        'boxStack': new Array(),
        'debug_': false
    },
    
    closeAll: function () {
        var count = this.get('count')
        for (var i=0; i<count; i++){
            var last = this.get('boxStack')[this.get('boxStack').length-1];
            last.destroy();
        }
    },
    
    getMaxZindex: function(){
    	var max = 0;
    	_.each(this.get('boxStack'), function(box, i){
    		max = Math.max(box.$el.css('z-index'), max);
    	});
    	return max;
    }
}); 
Utils.Lightbox.GLOBAL = new lightboxGlobal();


/*
 * lighytbox debug function
 */
var lbDebug = function(funcName, data) {
    if (Utils.Lightbox.GLOBAL.get('debug_') && typeof console != 'undefined' && typeof console.log != 'undefined') {
        console.log('Ligntbox.' + funcName, data);
    }
}


/*
 *  View for an individual lightbox
 *  TODO: zindex, ROUTER 
 */
Utils.Lightbox.View = Backbone.View.extend({
    
    model: Utils.Lightbox.GLOBAL, 
    
    /*
     * backbone functions
     */
    initialize: function (options) {
        _.bindAll(this, 'render', 'destroy', 'clickBg');
        _this = this;
        /*
         * default options
         */
        var defaults = {
    	      'width': "",
    	      'height': "",
    	      'bgColor': 'black_bg',
    	      'containerBgColor': '',
    	      'fadeIn': false,
    	      'fadeOut': false,
    	      'animationTime': 200,
    	      'verticalCenter': false,
    	      'showCloseBtn': false,
    	      'clickBgClose': true,
    	      'closeBtnClass': 'close_btn',
    	      'handle': null
    	    };
        this.options = _.extend(defaults, this.options);
        //set up model
        this.guid = guid();
        this.model.set({'count': this.model.get('count') + 1}, {silent: true});
        Utils.Lightbox.GLOBAL.get('boxStack').push(this);
        
        //initialize DOM element
        this.divId = this.model.get('divId') + this.model.get('count');
        var centered = this.options['verticalCenter'] ? 'centered' : '';
        var table = this.options['verticalCenter'] ? 'table' : 'none';
        var close_btn = this.options['showCloseBtn'] ?  '' : 'display:none;';
        $('body').append('<div class="lightbox '+ this.options['bgColor'] +'" id="'+ this.divId +'" style="display:'+ table +';"><div class="control"><a style="'+close_btn+'" href="" onclick="return false;" class="'+this.options['closeBtnClass']+'">X</a></div><div class="container '+ centered +'" style="display:none;background-color:'+ this.options['containerBgColor'] +';width:'+ this.options['width'] +'px"></div></div>');
        this.setElement('#'+this.divId)
        lbDebug('Add ' + this.divId + ':', this);
        lbDebug('Global stack: ' , this.model.get('boxStack'));
        
        //bind esc close
		var esc = function (e) {
            if (e.keyCode == 27) { 
                _this.destroy(); 
            };
			return e;
        };
        $(document).unbind('keyup', esc);
        $(document).bind('keyup', esc);
        
        
        if(this.options['handle'] != null) {//handle must be an Object !!
            this.options['handle']['val'] = this.$el;
        }
        
        //show the whole thing
        this.render();
    },
    
    events: {
        
        'click': 'clickBg',
        'click .close_btn': 'destroy'
    },
    
    render: function () {
        
        //inject html and set width of container to be the same as its child
        this.$('.container').html(this.options.innerHTML);
        this.$('.container').show();
		
		var bind_close_btn = this.options['bindCloseBtn'];
		if(bind_close_btn){
			this.$(bind_close_btn).click(this.destroy);
		}
		
		this.$('.container').children().css('margin-right','auto');
		this.$('.container').children().css('margin-left', 'auto');
        this.$el.show();
        

        //disable click to close for innerHTML
        this.$('.container').children().click(function(e){
            e.stopPropagation();
        });
        
        
        //make background of other lightboxes transparent; change scrolling target
        $('body').css('overflow', 'hidden');
        this.$el.css('overflow', 'auto');
        //$('.container', this.el).css('position', 'fixed'); chat
        
        $.each(this.model.get('boxStack'), $.proxy(function(key, val){
            if (val.guid != this.guid){
                //val.$el.css('background-color', 'transparent');
                // val.$el.removeClass(last.options['bgColor']);
                //disable scroll for others
                val.$el.css('overflow', 'hidden');
            }
        }, this));
        
        this.$('.'+this.options['closeBtnClass']).unbind('click', this.destroy);
        this.$('.'+this.options['closeBtnClass']).bind('click', this.destroy);
    },
    
    
    /*
     * terminate the lightbox
     */
    destroy: function () {
        //deduct count
        this.model.set({'count': this.model.get('count')-1}, {silent: true});
		var esc = function (e) {
            if (e.keyCode == 27) { 
                last.destroy(); 
            };
        };
        
        //show background for next front most lightbox and bind esc key and enable scroll for it
        if(this.model.get('boxStack').length > 1){
            var last = this.model.get('boxStack')[this.model.get('boxStack').length-2];
            last.$el.addClass(last.options['bgColor']);
            last.$el.css('overflow', 'auto');
            $(document).unbind('keyup', esc);
            $(document).bind('keyup', esc);
        }else{
            $('body').css('overflow', 'visible');
            $(document).unbind('keyup', esc);
        }
        
        // callback after function
		if (this.options['after']) {
			this.options['after'](this);
		}
        
        //remove light box
        if (this.options['fadeOut']){
            this.$('.container').fadeOut(this.options['animationTime'], $.proxy(function(){
                this.$el.fadeOut(this.options['animationTime'], $.proxy(function () {
                    this.$el.remove();
                }, this));    
            }, this));
            
        }else{
            this.$el.remove();
        };
		
        //delete objects
        this.model.get('boxStack').pop();
        lbDebug('Remove ' + this.divId + ':', this);
        lbDebug('Global stack: ' , this.model.get('boxStack'));
    },
    
    
    /*
     * register click background event
     */
    clickBg: function () {
        if (this.options['clickBgClose']){
            this.destroy();
        };
    }
});



/*
 * jQuery Interface
 */
(function($) {
    var methods = {
        init: function(options) {
            
            if (this.attr('href')){
                methods.ajax.apply(this, [options]);  
            }else{
                methods.inline.apply(this, [options]);
            };
            
            return this;
        },
        
        
        //passing only string as argument 
        inline: function(options) {
            if(typeof options === 'string'){
                this.click(function(){
                    $(document).ready(function(){
                        var lb = new Utils.Lightbox.View({innerHTML:options,
                                                      containerBgColor:'white',
                                                      verticalCenter:true});    
                    });
                        
                    return false;
                });
                return this;
                
            } else if (!options.innerHTML){
                $.error('Lightbox: Please set html content as innerHTML');
            };
            
            
            var do_show = function (options) {
                //do before 
                if (options && _.has(options, 'before')){
                    options['before']();
                }
                
                $(document).ready($.proxy(function(){
                    this.lb = new Utils.Lightbox.View(options);
                    //do callback 
                    if (options && _.has(options, 'callback')){
                        options['callback'](this.lb);
                    }
                },this));
                
                    
                return false;
            }
            
            
            if (options && _.has(options, 'instantShow') && options.instantShow){
                //do show lightbox
                do_show(options);
            }else{
                //register click event
                this.click(function(){
                    do_show(options);
                });
            };
            return this;
        },
        
        
        //using ajax mode
        ajax: function(options) {
            //connot find source of ajax url
            if (!this.attr('href') && !options.ajaxUrl){
                $.error('Lightbox: Please select an element with href attribute or provide ajaxUrl when using ajax method.');
            };
            
            //get ajax parameter
            if (options){
                var ajaxType = options.ajaxType ? options.ajaxType : 'GET';
                var ajaxData = options.ajaxData ? options.ajaxData : '' ;
                var ajaxUrl = options.ajaxUrl ? options.ajaxUrl : this.attr('href');    
            }else{
                var ajaxType = 'GET';
                var ajaxData = '' ;
                var ajaxUrl = this.attr('href');
            };
            
            
            //function that perform ajax
            var do_ajax = function (){
                //do before
                if (options && _.has(options, 'before')){
                    options['before']();
                }
                
                var $loading_bg = $('<div class="lightbox white_bg"><center class="lightbox_loading"></center></div>');
                $('body').append($loading_bg);
                $.ajax({
                    url: ajaxUrl,
                    type: ajaxType,
                    data: ajaxData,
                    dataType:'json',                    
                    success: function(response){
                    	$loading_bg.remove();
                        var lbOptions = options ? options : {};
                        lbOptions['innerHTML'] = response.innerHTML ? response.innerHTML : lbOptions['innerHTML'];
                        var lb = null;
                        $(document).ready(function(){
                            lb = new Utils.Lightbox.View(lbOptions);
                        });
                        
                        //do callback
                        if (options && _.has(options, 'callback')){
                            options['callback'](lb);
                        }
                        return false;
                    },
                    error: function( xhr ){
                    	$loading_bg.remove();
                        console.log(xhr);
                        return false;
                    }
                });
                return false;
            };
            
            if (options && _.has(options, 'instantShow') && options.instantShow){
                if (!_.has(options, 'ajaxUrl')){
                    $.error('Lightbox: Please indicate ajax url.');
                }
                
                //do ajax call
                do_ajax();
            }else{
                //register click event
                this.click(do_ajax);
            };
            return this;
        }
    }  


    //module interface
    $.fn.Lightbox = function(method){
        if (methods[method]){
            return methods[method].apply(this, Array.prototype.slice.call(arguments, 1));
        }else if (typeof method === 'string'){
            return methods.inline.apply( this, arguments );
        } else if (typeof method === 'object' || !method){
            return methods.init.apply( this, arguments );
        } else {
            $.error('Method ' +  method + ' does not exist on jQuery.Lightbox');
        }
        return this;
    };
	
	
	
    // Tooltip
    $.fn.tooltip = function(settings){
		var _this = this;
		var $el = $(this);
	    var _defaultSettings = {
			innerHtml: 'Test',
			bottom: 0,
			right: 0,
			id: 'tooltip',
			clean: false,
			neverShowThis: true,
			withDeco: true,
			useSlide: false,
			autoClose: false,
			noRepeat: true
	    };
		
		var _settings = $.extend(_defaultSettings, settings);
		
		if (_settings.clean) {
			// Delete/erase cookie
			deleteCookie(_settings.id);
		}
		
		if (getCookie(_settings.id)) {
			return;
		}
		
		if (_this.data(_settings.id+'Done')) {
			return;
		}
		
		
		if ($('#'+_settings.id).length!=0) {
			return this;
		}
		var $tip = $("<div></div>", {'class': 'tooltip', id: _settings.id});
		$tip.append("<div class='delete_btn'>X</div>");
		$tip.append(_settings.innerHtml);
		$tip.css({
			bottom: _settings.bottom,
			right: _settings.right,
			display: 'none'
		});
		if (_settings.neverShowThis) {
			$tip.append("<div class='neverShowThis'><span class='actChkBox fL'></span> <span class='msg'>Never show this again.</span></div>");
		}
		if (_settings.withDeco) {
			$tip.append("<div class='deco'></div>");
		}
		$el.append($tip)
		
		if (_settings.useSlide) {
			$tip.slideDown('slow', 'easeOutQuart');
		}
		else {
			$tip.fadeIn(400);
		}
		
		$tip.find('.delete_btn').bind('click', function(){
			if ($el.find('.actChkBox').hasClass('on')) {
				setCookie(_settings.id, true, 0);
			}
			else {
				if (_settings.noRepeat) {
					_this.data(_settings.id+'Done', true);
				}
			}
			
			if (_settings.useSlide) {
				$tip.slideUp('slow', function(){
					$tip.remove();
				});
			}
			else {
				$tip.fadeOut(300, function(){
					$tip.remove();
				});
			}
		});
		
		if (_settings.autoClose) {
			setTimeout(function(){$tip.find('.delete_btn').trigger('click');}, 3000);
		}
		
		
        return this;
    };
	

})( jQuery );

var ItemModel = Backbone.Model.extend({
	
	idAttribute: 'name',
	
	defaults: {
		name: '',
		cate: '',
		description: ''
	}
});

var ItemCollection = Backbone.Collection.extend({
	model: ItemModel,
	
	initialize: function(){
		_.bindAll(this, 'isOk');
	},
	
	isOk: function(){
		var result = true;
		_.each(this.models, function(item){
			if(!item.get('cate') || item.get('cate')==''){
				result = false;
				return false;
			}
		})
		return result;
	}
});

var Test1Collection = new ItemCollection([
    {name: 'gage', description: 'des gage'},
    {name: 'rita', description: 'des rita'},
    {name: 'love', description: 'des love'},
    {name: 'gage1', description: 'des gage1'},
    {name: 'rita1', description: 'des rita1'},
    {name: 'love1', description: 'des love1'},
    {name: 'gage2', description: 'des gage2'},
    {name: 'rita2', description: 'des rita2'},
    {name: 'love2', description: 'des love2'}
]);

var CateModel = Backbone.Model.extend({
	idAttribute: 'name',
	
	defaults: {
		name: '',
		items: {}
	},
	
	initialize: function(){
		_.bindAll(this, 'addItem', 'removeItem');
	},
	
	addItem: function(item){
		var tmp = this.get('items');
		tmp[item.get('name')] = item.get('name');
		this.set('items', tmp);
	},
	
	removeItem: function(item){
		var tmp = this.get('items');
		delete tmp[item.get('name')];
	}
});

var CateCollection = Backbone.Collection.extend({
	model: CateModel
});

var Test1CateCollection = new CateCollection([
    {name:'CLASS 1'},
    {name:'CLASS 2'},
    {name:'CLASS 3'},
]);

var ItemView = Backbone.View.extend({
	
	initialize: function(options){
		_.bindAll(this, 'onInfo');
		this.name = options.name || 'no name';
		this.description = options.description || 'no description';
		this.$el.data('view', this);
		this.cate = '';
	},

	events: {
		'click .info': 'onInfo'
	},
	
	onInfo: function(e){
		console.log(2233);
		if(e){
			var tmp = _.template($('#template_info_tip').html());
			var tmpHtml = tmp({title:this.name, description:this.description});
			$.fn.Lightbox('inline', {
	            instantShow: true,
	            innerHTML: tmpHtml,
	            bgColor: 'white_bg',
	            verticalCenter: true
	        });
		}
	}
})

function receiveAction(e, ui){
	var view = ui.item.data('view');
	var t_view = $(e.target).parents('.sorting-class').data('view');
	if(t_view){
		view.cate = t_view.name;
		view.model.set('cate', t_view.name);
		t_view.model.addItem(view.model);
	}else{
		view.cate = '';
		view.model.set('cate', '');
		var sender_view = ui.sender.parents('.sorting-class').data('view');
		sender_view.model.removeItem(view.model);
	}
	if(Test1Collection.isOk()){
		$('.main-next').addClass('ok');
	}else{
		$('.main-next').removeClass('ok');
	}
}

var CateView = Backbone.View.extend({
	
	initialize: function(options){
		_.bindAll(this, 'onChangeName', '_validate', '_saveText', 'onBlur', 'onEnter');
		this.name = options.name;
		this.isnew = options.isnew;
		this.$label = this.$el.find('h3>span');
		this.$input = this.$el.find('h3>input');
		this.$el.data('view', this);
		if(this.isnew){
			this.onChangeName();
		}
	},
	
	events: {
		'click h3>span': 'onChangeName',
		'blur h3>input': 'onBlur',
		'keyup h3>input': 'onEnter'
	},
	
	onChangeName: function(){
		this.$label.hide();
		this.$input.val(this.name);
		this.$input.show();
		this.$input.focus();
	},
	
	_validate: function(v){
		var ok = true;
		$('.sorting-class').each(function(i, obj){
			if($(obj).find('h3>span').text() == v){
				ok = false;
				return false;
			}
		});
		return ok;
	},
	
	_saveText: function(){
		var value = this.$input.val().trim();
		if(value && this._validate(value)){
			this.name = value;			
		}else{
			if(this.isnew){
				this.$el.remove();
			}
		}
		this.$label.text(this.name);
		this.$input.hide();
		this.$label.show();
		if(this.isnew){
			this.$(".sorting-items").sortable({
		        connectWith: ".connectedSortable",
	        	receive: receiveAction,
		    }).disableSelection();
			this.isnew = false;
		}
	},
	
	onBlur: function(e){
		if(e){
			this._saveText();
		}
	},
	
	onEnter: function(e){
		if(e.keyCode == 13)
			this._saveText();
	}
	
});


var LeftControlView = Backbone.View.extend({
	
	el: '.main-bd .main-left .sorting-items',
	
	initialize: function(options){
		_.bindAll(this, 'render');
		this.render();
	},
	
	render: function(){
		var _this = this;
		_.each(this.collection.models, function(item){
			var that = $('<li><span class="name">'+item.get('name')+'</span><span class="info">?</span>');
			_this.$el.append(that);
			item.view = new ItemView({
	    		el: that,
	    		name: item.get('name'),
	    		description: item.get('description'),
	    		model: item
	    	});
		});
	}
	
});


var AllClassesView = Backbone.View.extend({
	el: '.main-bd .main-right',
	
	initialize: function(options){
		_.bindAll(this, 'render');
		this.render();
	},
	
	render: function(){
		var _this = this;
		var tmp = _.template($('#template_sorting_class').html());
		
		_.each(this.collection.models, function(cate){
			var tmpHtml = tmp({name:cate.get('name')});
			var that = $(tmpHtml);
			_this.$el.append(that);
			cate.view = new CateView({
	    		el: that,
	    		name: cate.get('name'),
	    		isnew: false,
	    		model:cate
	    	});
		});
	}
});


function resize_all(){
	var h = Math.max(274, $(window).height()-60);
	var w = Math.max(236, $(window).width()-238);
	$('.main-left, .main-left .sorting-items').height(h);
	$('.main-right').width(w);
}


$(function() {
	resize_all();
	
	$(window).resize($.debounce(100,resize_all));
	
//	$.fn.Lightbox('inline', {
//        instantShow: true,
//        innerHTML: $('#template_introduce1').html(),
//        bgColor: 'white_bg',
//        verticalCenter: true
//    });
	
	var leftControlView = new LeftControlView({
		collection: Test1Collection
	});
	
    var allClassesView = new AllClassesView({
    	collection: Test1CateCollection
    });
	
    $(".sorting-items").sortable({
        connectWith: ".connectedSortable",
        items: "li:not(.title)",
        receive: receiveAction
    }).disableSelection();
    
    $('.main-hd button.main-info').click(function(){
    	$.fn.Lightbox('inline', {
            instantShow: true,
            innerHTML: $('#template_introduce1').html(),
            bgColor: 'white_bg',
            verticalCenter: true
        });
    });
    
    $('.main-right .add-new').click(function(){
    	var newklass = $($('#template_klass').html());
    	$(this).after(newklass);
    	new CateView({
    		el: newklass,
    		name: newklass.find('h3>span').text(),
    		isnew: true
    	});
    });
    
    var layoutController = new WfView({el:$('.main-right')});
    
    
});



