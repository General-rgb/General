from flask import Flask, render_template, request, abort, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'guoqingxi_curtain_shop_2023'  # 用于会话和flash消息的密钥

@app.route('/')
def index():
    # 首页产品数据
    featured_products = [
        {
            'id': 1,
            'name': '欧式豪华窗帘',
            'description': '高端定制欧式风格，为您的家居增添奢华感',
            'image': 'curtain-1.jpg'
        },
        {
            'id': 2,
            'name': '现代简约窗帘',
            'description': '简约不简单，彰显现代家居的时尚美感',
            'image': 'curtain-2.jpg'
        },
        {
            'id': 3,
            'name': '儿童房窗帘',
            'description': '色彩丰富，图案可爱，为孩子创造梦幻空间',
            'image': 'curtain-3.jpg'
        },
        {
            'id': 4,
            'name': '智能电动窗帘',
            'description': '一键控制，智能家居的理想选择',
            'image': 'curtain-4.jpg'
        }
    ]
    
    # 服务流程数据
    process_steps = [
        {
            'icon': 'fa-clipboard-list',
            'title': '免费咨询',
            'description': '电话或到店咨询，我们的专业顾问将为您提供窗帘选择建议'
        },
        {
            'icon': 'fa-ruler',
            'title': '上门测量',
            'description': '专业人员上门精确测量窗户尺寸，确保窗帘完美契合'
        },
        {
            'icon': 'fa-cut',
            'title': '定制生产',
            'description': '根据您的需求和测量结果，精心裁剪制作高品质窗帘'
        },
        {
            'icon': 'fa-truck',
            'title': '安装服务',
            'description': '专业安装团队上门安装，确保窗帘安装牢固美观'
        }
    ]
    
    # 客户评价数据
    testimonials = [
        {
            'id': 1,
            'name': '王女士',
            'avatar': 'avatar-1.jpg',
            'comment': '窗帘质量非常好，安装师傅也很专业，整个过程非常满意。',
            'rating': 5
        },
        {
            'id': 2,
            'name': '李先生',
            'avatar': 'avatar-2.jpg',
            'comment': '价格合理，款式新颖，安装迅速，非常推荐这家店！',
            'rating': 5
        },
        {
            'id': 3,
            'name': '张女士',
            'avatar': 'avatar-3.jpg',
            'comment': '定制的窗帘完全符合我的期望，质量和做工都很棒。',
            'rating': 5
        }
    ]
    
    shop_info = {
        'name': '北京国清曦窗帘加工部',
        'phone': '13716958774',
        'address': '北京市顺义区李遂镇沟北村二条二十八号',
        'email': '2568055317@qq.com',
        'hours': {
            '周一至周五': '9:00 - 18:00',
            '周六': '9:00 - 17:00',
            '周日': '10:00 - 16:00'
        }
    }
    
    return render_template(
        'index.html', 
        featured_products=featured_products,
        process_steps=process_steps,
        testimonials=testimonials,
        shop_info=shop_info
    )

@app.route('/products')
def products():
    # 产品分类
    categories = [
        {'id': 'curtains', 'name': '窗帘'},
        {'id': 'sheers', 'name': '窗纱'},
        {'id': 'blinds', 'name': '百叶窗'},
        {'id': 'rollers', 'name': '卷帘'},
        {'id': 'accessories', 'name': '窗帘配件'}
    ]
    
    # 产品数据
    all_products = [
        {
            'id': 1,
            'name': '欧式豪华窗帘',
            'category': 'curtains',
            'description': '高端定制欧式风格，为您的家居增添奢华感。采用优质面料，做工精细，褶皱丰富，悬垂感强。',
            'features': ['防尘', '隔音', '遮光性好'],
            'suitable_for': ['客厅', '卧室', '书房'],
            'images': ['curtain-1.jpg', 'curtain-1-detail.jpg', 'curtain-1-room.jpg'],
            'is_featured': True
        },
        {
            'id': 2,
            'name': '现代简约窗帘',
            'category': 'curtains',
            'description': '简约不简单，彰显现代家居的时尚美感。线条流畅，色彩纯净，为空间带来轻盈感。',
            'features': ['易清洗', '防褪色', '透光性好'],
            'suitable_for': ['客厅', '卧室', '餐厅'],
            'images': ['curtain-2.jpg', 'curtain-2-detail.jpg', 'curtain-2-room.jpg'],
            'is_featured': True
        },
        {
            'id': 3,
            'name': '儿童房窗帘',
            'category': 'curtains',
            'description': '色彩丰富，图案可爱，为孩子创造梦幻空间。采用环保面料，安全健康，呵护孩子成长。',
            'features': ['环保材质', '色彩鲜艳', '图案丰富'],
            'suitable_for': ['儿童房'],
            'images': ['curtain-3.jpg', 'curtain-3-detail.jpg', 'curtain-3-room.jpg'],
            'is_featured': True
        },
        {
            'id': 4,
            'name': '智能电动窗帘',
            'category': 'curtains',
            'description': '一键控制，智能家居的理想选择。支持手机APP控制，可定时开关，让生活更便捷。',
            'features': ['远程控制', '静音电机', '定时功能'],
            'suitable_for': ['客厅', '卧室', '办公室'],
            'images': ['curtain-4.jpg', 'curtain-4-detail.jpg', 'curtain-4-room.jpg'],
            'is_featured': True
        },
        {
            'id': 5,
            'name': '轻薄透光窗纱',
            'category': 'sheers',
            'description': '轻盈透光，保护隐私的同时让阳光温柔洒入。面料轻薄，手感柔软，为空间增添柔和质感。',
            'features': ['透光性好', '柔软质地', '易于清洗'],
            'suitable_for': ['客厅', '卧室', '书房'],
            'images': ['sheer-1.jpg', 'sheer-1-detail.jpg', 'sheer-1-room.jpg'],
            'is_featured': False
        },
        {
            'id': 6,
            'name': '提花窗纱',
            'category': 'sheers',
            'description': '精致提花工艺，为窗户增添艺术气息。图案优雅，质地轻盈，既能保护隐私又不阻挡光线。',
            'features': ['提花工艺', '高端质感', '柔和光线'],
            'suitable_for': ['客厅', '卧室', '餐厅'],
            'images': ['sheer-2.jpg', 'sheer-2-detail.jpg', 'sheer-2-room.jpg'],
            'is_featured': False
        },
        {
            'id': 7,
            'name': '铝合金百叶窗',
            'category': 'blinds',
            'description': '经典铝合金百叶窗，坚固耐用，调光方便。可精确控制光线角度，保护隐私同时保证室内明亮。',
            'features': ['耐用', '易调节', '防尘防潮'],
            'suitable_for': ['卧室', '书房', '办公室'],
            'images': ['blind-1.jpg', 'blind-1-detail.jpg', 'blind-1-room.jpg'],
            'is_featured': False
        },
        {
            'id': 8,
            'name': '木质百叶窗',
            'category': 'blinds',
            'description': '天然木材制作，温润质感，为家居增添自然气息。手工精细打磨，结实耐用，色泽温暖。',
            'features': ['天然木材', '手工打磨', '色泽温暖'],
            'suitable_for': ['卧室', '书房', '客厅'],
            'images': ['blind-2.jpg', 'blind-2-detail.jpg', 'blind-2-room.jpg'],
            'is_featured': False
        },
        {
            'id': 9,
            'name': '遮光卷帘',
            'category': 'rollers',
            'description': '优质遮光面料，几乎100%遮光效果，为您创造完美睡眠环境。操作简便，卷收整齐不占空间。',
            'features': ['全遮光', '简约设计', '节省空间'],
            'suitable_for': ['卧室', '影音室'],
            'images': ['roller-1.jpg', 'roller-1-detail.jpg', 'roller-1-room.jpg'],
            'is_featured': False
        },
        {
            'id': 10,
            'name': '透光卷帘',
            'category': 'rollers',
            'description': '精选透光面料，柔和阳光，减少眩光。现代简约设计，操作便捷，适合多种室内空间。',
            'features': ['透光性好', '防紫外线', '现代设计'],
            'suitable_for': ['客厅', '书房', '餐厅'],
            'images': ['roller-2.jpg', 'roller-2-detail.jpg', 'roller-2-room.jpg'],
            'is_featured': False
        },
        {
            'id': 11,
            'name': '窗帘杆套装',
            'category': 'accessories',
            'description': '精美窗帘杆套装，包含窗帘杆、挂钩和固定件。多种材质和颜色可选，适配各类窗帘和装修风格。',
            'features': ['多种材质', '安装简便', '承重力强'],
            'suitable_for': ['所有窗帘类型'],
            'images': ['acc-1.jpg', 'acc-1-detail.jpg', 'acc-1-room.jpg'],
            'is_featured': False
        },
        {
            'id': 12,
            'name': '窗帘挂钩和夹子',
            'category': 'accessories',
            'description': '高品质窗帘挂钩和装饰夹子，美观实用，安装便捷。可用于各类窗帘的悬挂和造型装饰。',
            'features': ['多种款式', '坚固耐用', '装饰性强'],
            'suitable_for': ['所有窗帘类型'],
            'images': ['acc-2.jpg', 'acc-2-detail.jpg'],
            'is_featured': False
        }
    ]
    
    # 从URL获取分类过滤参数
    category_filter = request.args.get('category', None)
    
    # 如果有分类过滤，则筛选产品
    if category_filter:
        filtered_products = [p for p in all_products if p['category'] == category_filter]
    else:
        filtered_products = all_products
    
    return render_template(
        'products.html',
        categories=categories,
        products=filtered_products,
        current_category=category_filter
    )

@app.route('/cases')
def cases():
    return render_template('cases.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/map')
def map_view():
    return render_template('map.html')

@app.route('/products/<int:product_id>')
def product_detail(product_id):
    # 产品数据（在实际应用中，这应该从数据库中获取）
    all_products = [
        {
            'id': 1,
            'name': '欧式豪华窗帘',
            'category': 'curtains',
            'description': '高端定制欧式风格，为您的家居增添奢华感。采用优质面料，做工精细，褶皱丰富，悬垂感强。',
            'features': ['防尘', '隔音', '遮光性好'],
            'suitable_for': ['客厅', '卧室', '书房'],
            'images': ['curtain-1.jpg', 'curtain-1-detail.jpg', 'curtain-1-room.jpg'],
            'is_featured': True
        },
        {
            'id': 2,
            'name': '现代简约窗帘',
            'category': 'curtains',
            'description': '简约不简单，彰显现代家居的时尚美感。线条流畅，色彩纯净，为空间带来轻盈感。',
            'features': ['易清洗', '防褪色', '透光性好'],
            'suitable_for': ['客厅', '卧室', '餐厅'],
            'images': ['curtain-2.jpg', 'curtain-2-detail.jpg', 'curtain-2-room.jpg'],
            'is_featured': True
        },
        {
            'id': 3,
            'name': '儿童房窗帘',
            'category': 'curtains',
            'description': '色彩丰富，图案可爱，为孩子创造梦幻空间。采用环保面料，安全健康，呵护孩子成长。',
            'features': ['环保材质', '色彩鲜艳', '图案丰富'],
            'suitable_for': ['儿童房'],
            'images': ['curtain-3.jpg', 'curtain-3-detail.jpg', 'curtain-3-room.jpg'],
            'is_featured': True
        },
        {
            'id': 4,
            'name': '智能电动窗帘',
            'category': 'curtains',
            'description': '一键控制，智能家居的理想选择。支持手机APP控制，可定时开关，让生活更便捷。',
            'features': ['远程控制', '静音电机', '定时功能'],
            'suitable_for': ['客厅', '卧室', '办公室'],
            'images': ['curtain-4.jpg', 'curtain-4-detail.jpg', 'curtain-4-room.jpg'],
            'is_featured': True
        },
        {
            'id': 5,
            'name': '轻薄透光窗纱',
            'category': 'sheers',
            'description': '轻盈透光，保护隐私的同时让阳光温柔洒入。面料轻薄，手感柔软，为空间增添柔和质感。',
            'features': ['透光性好', '柔软质地', '易于清洗'],
            'suitable_for': ['客厅', '卧室', '书房'],
            'images': ['sheer-1.jpg', 'sheer-1-detail.jpg', 'sheer-1-room.jpg'],
            'is_featured': False
        },
        {
            'id': 6,
            'name': '提花窗纱',
            'category': 'sheers',
            'description': '精致提花工艺，为窗户增添艺术气息。图案优雅，质地轻盈，既能保护隐私又不阻挡光线。',
            'features': ['提花工艺', '高端质感', '柔和光线'],
            'suitable_for': ['客厅', '卧室', '餐厅'],
            'images': ['sheer-2.jpg', 'sheer-2-detail.jpg', 'sheer-2-room.jpg'],
            'is_featured': False
        },
        {
            'id': 7,
            'name': '铝合金百叶窗',
            'category': 'blinds',
            'description': '经典铝合金百叶窗，坚固耐用，调光方便。可精确控制光线角度，保护隐私同时保证室内明亮。',
            'features': ['耐用', '易调节', '防尘防潮'],
            'suitable_for': ['卧室', '书房', '办公室'],
            'images': ['blind-1.jpg', 'blind-1-detail.jpg', 'blind-1-room.jpg'],
            'is_featured': False
        },
        {
            'id': 8,
            'name': '木质百叶窗',
            'category': 'blinds',
            'description': '天然木材制作，温润质感，为家居增添自然气息。手工精细打磨，结实耐用，色泽温暖。',
            'features': ['天然木材', '手工打磨', '色泽温暖'],
            'suitable_for': ['卧室', '书房', '客厅'],
            'images': ['blind-2.jpg', 'blind-2-detail.jpg', 'blind-2-room.jpg'],
            'is_featured': False
        },
        {
            'id': 9,
            'name': '遮光卷帘',
            'category': 'rollers',
            'description': '优质遮光面料，几乎100%遮光效果，为您创造完美睡眠环境。操作简便，卷收整齐不占空间。',
            'features': ['全遮光', '简约设计', '节省空间'],
            'suitable_for': ['卧室', '影音室'],
            'images': ['roller-1.jpg', 'roller-1-detail.jpg', 'roller-1-room.jpg'],
            'is_featured': False
        },
        {
            'id': 10,
            'name': '透光卷帘',
            'category': 'rollers',
            'description': '精选透光面料，柔和阳光，减少眩光。现代简约设计，操作便捷，适合多种室内空间。',
            'features': ['透光性好', '防紫外线', '现代设计'],
            'suitable_for': ['客厅', '书房', '餐厅'],
            'images': ['roller-2.jpg', 'roller-2-detail.jpg', 'roller-2-room.jpg'],
            'is_featured': False
        },
        {
            'id': 11,
            'name': '窗帘杆套装',
            'category': 'accessories',
            'description': '精美窗帘杆套装，包含窗帘杆、挂钩和固定件。多种材质和颜色可选，适配各类窗帘和装修风格。',
            'features': ['多种材质', '安装简便', '承重力强'],
            'suitable_for': ['所有窗帘类型'],
            'images': ['acc-1.jpg', 'acc-1-detail.jpg', 'acc-1-room.jpg'],
            'is_featured': False
        },
        {
            'id': 12,
            'name': '窗帘挂钩和夹子',
            'category': 'accessories',
            'description': '高品质窗帘挂钩和装饰夹子，美观实用，安装便捷。可用于各类窗帘的悬挂和造型装饰。',
            'features': ['多种款式', '坚固耐用', '装饰性强'],
            'suitable_for': ['所有窗帘类型'],
            'images': ['acc-2.jpg', 'acc-2-detail.jpg'],
            'is_featured': False
        }
    ]
    
    # 查找指定ID的产品
    product = next((p for p in all_products if p['id'] == product_id), None)
    
    # 如果找不到产品，返回404
    if not product:
        abort(404)
    
    # 获取产品分类信息
    categories = [
        {'id': 'curtains', 'name': '窗帘'},
        {'id': 'sheers', 'name': '窗纱'},
        {'id': 'blinds', 'name': '百叶窗'},
        {'id': 'rollers', 'name': '卷帘'},
        {'id': 'accessories', 'name': '窗帘配件'}
    ]
    
    # 获取产品的分类名称
    category_name = next((c['name'] for c in categories if c['id'] == product['category']), '未分类')
    
    # 获取相关产品（同一分类的其他产品）
    related_products = [p for p in all_products if p['category'] == product['category'] and p['id'] != product_id][:4]
    
    return render_template(
        'product_detail.html',
        product=product,
        category_name=category_name,
        related_products=related_products
    )

@app.route('/submit-consultation', methods=['POST'])
def submit_consultation():
    # 获取表单数据
    product_id = request.form.get('product_id')
    product_name = request.form.get('product_name')
    name = request.form.get('name')
    phone = request.form.get('phone')
    address = request.form.get('address')
    message = request.form.get('message')
    
    # 在实际应用中，这里应该将咨询信息保存到数据库
    # 并且可能会发送通知邮件给管理员
    
    # 演示版本，只返回成功消息
    flash('您的咨询已提交成功，我们将尽快与您联系！', 'success')
    
    # 重定向回产品详情页
    return redirect(url_for('product_detail', product_id=product_id))

@app.route('/submit-contact', methods=['POST'])
def submit_contact():
    # 获取表单数据
    name = request.form.get('name')
    phone = request.form.get('phone')
    email = request.form.get('email')
    message = request.form.get('message')
    
    # 在实际应用中，这里应该将留言信息保存到数据库
    # 并且可能会发送通知邮件给管理员
    
    # 演示版本，只返回成功消息
    flash('您的留言已提交成功，我们将尽快与您联系！', 'success')
    
    # 重定向回联系页面
    return redirect(url_for('contact'))

if __name__ == '__main__':
    app.run(debug=True)