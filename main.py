import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="QUANTUM COMPUTER NEGATIVE IMPACT TO CURRENT INFORMATION SECURITY",
    page_icon="./assets/icons/favicon.ico",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.write(
    """
    <style>
    .container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
    }
    .img-container {
        margin-bottom: 20px;
    }
      h1 {
        font-size: 80px;
    }
    </style>
    <div class="container">
        <div class="img-container">
            <img src="https://assets-global.website-files.com/6523f13a748909d3e1bbb657/65dc67a2b4f8cf8b5f750534_technology-quantum-computing-is-now.png" width="700" style="channels='RGB'">
        </div>
        <h1>QUANTUM COMPUTER NEGATIVE IMPACT TO CURRENT INFORMATION SECURITY</h1>
    </div>
    """,
    unsafe_allow_html=True
)

with st.sidebar:
    st.header("Nội dung bài viết")
    source_vid = st.sidebar.write("""
    <style>
        .toc {
            background-color: #0E1117;
            border-radius: 10px;
        }
        .toc p {
            font-size: 15px;
            margin: 0;
            padding: 10px;
            cursor: pointer;
            z-index: 2;
        }
        # .toc p:nth-child(odd) {
        #     background-color: #F1F1EF; /* Màu nền cho các hàng lẻ */
        # }
        # .toc p:nth-child(even) {
        #     background-color: #262730; /* Màu nền cho các hàng chẵn */
        # }
    </style>
    <div class="toc">
        <p>1. Máy tính lượng tử và máy tính cổ điển. </p>
        <p>2. Sự đe doạ của máy tính lượng tử đến công nghệ bảo  mật thông tin cổ điển.</p>
        <p>3. Mặt tích cực cùng những ứng dụng của máy tính lượng  tử. </p>
        <p>4. Thành tựu đã đạt được đến hiện nay của Máy tính lượng  tử. </p>
        <p>5. Vì sao Máy tính Lượng tử chưa được sử dụng rộng rãi?</p>
        <p>6. Kết luận</p>
    </div>
    """, unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["Post", "Demo", "Reference"])

with tab1:
    st.markdown("<h2 style='color: #FFC81B;'>F-Code [Techaway 2024]</h2>", unsafe_allow_html=True)
    st.markdown("#### **F-Code authors:**")
    st.write("""
        - *Lê Hoàng Trang Nhã - F19*
        - *Đặng Nguyễn Thảo Nhi - F19*
    """)
    st.header("Introduction")
    st.write("Chào mừng các bạn đến với chuyến phiêu lưu kì lạ cùng Trang Nhã và Thảo Nhi vào vùng  đất của điện toán lượng tử, nơi mà tất cả logic đi nghỉ dưỡng dài kỳ ở Phan Thiết và xác suất  thì như vừa mới nốc một đống steroid.")

    st.markdown("<h2 style='color: #51C95D;'>1. Máy tính lượng tử và máy tính cổ điển.</h2>", unsafe_allow_html=True)
    st.write("""
   *Máy tính lượng tử* là những mô hình tính toán có bản chất khác hoàn toàn so với  mô hình tính toán cổ điển của máy tính thông thường. Khác biệt lớn nhất giữa hai  mô hình trên là trong khi máy tính truyền thống dựa vào các bit nhị phân, kí hiệu  là 0 và 1, để xử lý thông tin; thì máy tính lượng tử sử dụng đơn vị thông tin gọi là qubit hay quantum bit làm nền tảng. Nó được dựa trên nguyên lý về sự chồng  chập (superimposition) và sự liên đới (entanglement), tức là thay vì chỉ có thể nhận được một trong hai giá trị 0 và 1 như máy tính thông thường, thì nguyên lý trên giúp một qubit thể hiện được cả 0 và 1 cùng một lúc, như con mèo của  Schrodinger - nó sẽ đồng thời vừa sống và vừa chết trong khoảnh khắc bạn mở
   chiếc hộp ra, nhưng trong trường hợp này là chạy chương trình1; cùng với đó là sự kết nối giữa các qubit khiến cho trạng thái qubit này thay đổi dựa vào qubit còn  lại, không quan trọng khoảng cách. Qua đó, công nghệ máy tính lượng tử nhảy vọt  từ xử lý kép sang xử lý đa biến giúp tăng tốc độ tính toán theo cấp số nhân, từ đó giải quyết được những vấn đề phức tạp chỉ trong vài giây, trong khi máy tính cổ điển phải mất hàng chục đến hàng trăm nghìn năm để hoàn thành, và khả năng  xử lý này là vô hạn. 


    Thật ngạc nhiên khi biết được rằng, một con quái vật với khả năng gần như vô hạn như vậy đã không còn là sản phẩm của trí tưởng tượng hay chỉ trên lý thuyết  nữa, nó thật sự tồn tại. Mẫu máy tính lượng tử đầu tiên mang tên D Wave One  được công bố vào ngày 11 tháng 5 năm 2011.Lấy đó làm tiền đề, qua nhiều năm,  công ty điện toán lượng tử D-Wave ở Canada đã đưa những chiếc máy tính lượng  tử thương mại ra thị trường với giá 10 triệu USD (hiện nay cty đã dừng bán máy  tính vật lý mà chuyển sang cung cấp quyền truy cập vào khả năng tính toán lượng  tử thông qua đám mây). Hay gần đây nhất, nhóm nghiên cứu của Google đã trình  làng công chúng một siêu máy tính lượng tử - Sycamore. 
    """)

    st.markdown("<h2 style='color: #51C95D;'>2. Sự đe doạ của máy tính lượng tử đến công nghệ bảo  mật thông tin cổ điển.</h2>", unsafe_allow_html=True)
    st.write("""
    Qua phần trước, các bạn đã hiểu được về Máy tính lượng tử và điện toán của nó - nơi các quy tắc của điện toán cổ điển thực hiện một bước nhảy vọt đến phi  thường và vô lý. Vậy thì sự phát triển công nghệ điên rồ này sẽ ảnh hưởng thế nào  đến lĩnh vực bảo mật thông tin hiện nay?
    
    Giờ hãy tưởng tượng cái máy tính tiêu chuẩn của bạn như một lâu đài thời trung  cổ, với một bức tường dày, hào nước, có lính canh được trang bị vũ khí. Anh bạn  Máy tính Lượng tử trong trường hợp đó sẽ như một con ma có khả năng xuyên  tường, dịch chuyển tức thời và cười nhạo lính gác trong khi nhấp trà. 
    """)

    st.image("./assets/images/download.jpg", width=850, channels="RGB", caption="https://news.microsoft.com/vi-vn/2018/03/06/4-phut-de-hieu-ro-ve-may-tinh-luong-tu-quantum-computing/")

    st.write("""
    Không những vậy, nếu tương tác web là một trò high-stake poker game, thay vì bluffing, máy tính lượng tử có thể nhìn thấy tất cả lá bài của bạn nhanh hơn. Hầu  hết công nghệ bảo mật đều dựa trên việc chúng ta hiện tại không thể nhanh chóng  tìm ra các thừa số nguyên tố của một khóa. Máy tính lượng tử có thể bẻ khóa các  khóa mật mã hiện tại một cách nhanh chóng, do đó mọi tương tác web hiện có đều  gặp rủi ro. Những kẻ tấn công có động cơ có thể tận dụng một số lượng nhỏ máy  tính lượng tử để gây ra thiệt hại trên diện rộng [2]. 
    
    Ngày nay mọi sự vận hành trong cuộc sống sinh hoạt hằng ngày hầu hết đều sử dụng internet, chúng ta đều đã ít nhất một lần sử dụng nó cho việc liên lạc, giải trí,  mua sắm, etc. Và ai cũng có vài tài khoản internet nào đó như tài khoản ngân  hàng, email, game, mạng xã hội hoặc bất kỳ ứng dụng nào. Đi kèm với sự tiện  dụng và độ phủ sóng rộng rãi chính là vấn đề bảo mật thông tin. Đa phần mật  khẩu của tài khoản chúng ta được mã hoá và đưa vào lưu trữ ở một nơi nào đó;  dù đã có những vụ tấn công xâm nhập vào các lỗ hổng của máy chủ để hack dữ liệu, nhưng trên lý thuyết thì các dữ liệu đã được mã hoá sẽ cực kỳ khó bẻ khoá
    
    Cho dù nó đang ở trạng thái nghỉ hay đang được truyền tải giữa các thiết bị. Nó được tin tưởng đến mức một số tổ chức chính phủ, quốc gia hay thậm chí là quân  đội sử dụng để lưu trữ nhiều dữ liệu nhạy cảm như tài liệu mật, số an sinh xã hội,  vân vân.
    
    An toàn thông tin sẽ bảo vệ những thông tin, dữ liệu khỏi việc bị rò rỉ ra bên ngoài,  bị sửa đổi trái phép và đảm bảo được tính toàn diện khi đến được tay người dùng.  Mật mã (cryptography) là một trong những lĩnh vực trọng yếu trong việc bảo mật  
    thông tin, đó là quá trình bảo mật dữ liệu và thông tin liên lạc giữa hai bên giao  tiếp trước bất kỳ sự tấn công nào, nó cung cấp độ bảo mật (confidentiality), tính  toàn vẹn (integrity) và độ xác thực (authentication). Có hai loại thuật toán mật mã chính, thuật toán đối xứng (symmetric) và thuật toán bất đối xứng (asymmetric).  Thuật toán đối xứng ít yếu tố tính toán chuyên sâu, nó dùng chung key cho cả việc mã hoá và giải mã; ngược lại, thuật toán bất đối xứng sẽ yêu cầu nhiều về việc tính toán chuyên sâu và sử dụng hai loại key khác nhau, một key công khai  và một key ẩn, cho việc mã hoá và giải mã. 
    
    Tính bảo mật của mật mã hiện nay phụ thuộc vào độ khó trong việc phân tích các  số nguyên tố lớn và thách thức trong việc giải quyết những bài toán logarit rời rạc  được cho là khó ‘chữa’. Với những thuật toán mã hoá phức tạp hoặc được khai  triển với quá nhiều quy tắc và logic, những kẻ xâm nhập sẽ mất rất nhiều thời gian  để giải mã, trong khi đấy các cuộc tấn công mạng thường chỉ diễn ra trong vài  phút thậm chí là vài giây, vì thế mã hoá bảo mật vẫn sẽ còn an toàn, ít nhất là trong thời điểm hiện tại. Với sự ra đời của thuật toán Shor càng làm dấy lên các  mối lo ngại cho người dùng nói chung và cộng đồng an ninh mạng nói riêng, vì thuật toán đã cho thấy sức mạnh xử lý kinh hoàng của máy tính lượng tử sẽ khiến  các thuật toán mã hoá hiện nay dễ dàng bị tấn công vét cạn (brute-force attack),  qua đó tác động tiêu cực vào độ bảo mật của thuật toán mã hoá cổ điển hiện  nay. Dựa vào tốc độ phát triển của máy tính lượng tử với sức mạnh vượt trội, nó chỉ cần vài phút để phá vỡ các hàng rào mã hoá bảo mật cực kỳ phức tạp, cơ quan an ninh quốc gia Mỹ cho biết: “Một máy tính lượng tử đủ lớn sẽ có khả năng  phá hoại tất cả các thuật toán khoa học đang được sử dụng rộng rãi, đe doạ những 
    thứ như nghiên cứu công nghiệp, dược phẩm và các tình báo tối mật của chính phủ [3]
    
    Mật mã được ứng dụng nhiều trong thực tiễn như là tài chính, giao dịch ngân  hàng, bảo mật mật khẩu, thẻ ATM hay thương mại điện tử. Chính vì tính phổ biến  của mật mã bảo mật nên việc bị tác động tiêu cực sẽ gây ra rủi ro, đe doạ trực  tiếp đến các hoạt động kinh doanh trên cùng những tổ chức đang sử dụng hình  thức bảo mật này. Ngoài ra, mối đe doạ đến từ tấn công thông tin trên mạng kỹ thuật số đang gia tăng đáng kể, dẫn đến việc gây thêm áp lực cho các doanh  nghiệp trong công cuộc tăng cường, củng cố thế trận an ninh của họ. Vào đầu  năm 2023, quốc hội Mỹ đã thông qua đạo luật về bảo mật thông tin, bắt buộc tất cả các cơ quan gần như phải chuyển đổi ngay lập tức các phương pháp mã hoá mà máy tính lượng tử không thể phá vỡ [4].  
    
    Đào sâu vào trong lĩnh vực mã hoá, khi dữ liệu được mã hóa (encrypt) bằng thuật  toán mật mã hóa (cryptographic algorithm), ta không thể diễn giải nó hoặc đoán  nội dung ban đầu của dữ liệu từ văn bản thô (ciphertext), đảm bảo dữ liệu được  bảo mật khỏi những con mắt tò mò. Chúng ta có hình thức mã hoá lâu đời nhất - mã hoá đối xứng hay mã hoá riêng (private key). Đây là một loại sơ đồ mã hoá dùng cùng một key để vừa mã hóa và giải mã các tệp tin hay dữ liệu. Cách thức  hoạt động của mã hoá đối xứng là chia sẻ một key với hai hay nhiều người dùng  với nhau để giải - mã hoá các văn bản thô. Quá trình sẽ là chạy văn bản thô (plaintext) là đầu vào, thông qua thuật mật mã (cipher) sẽ lần lượt tạo ra các bản  mã (ciphertext) là đầu ra. Khó khăn mà hình thức mã hoá này gặp phải chính là làm sao để chia sẻ key an toàn và phải đảm bảo thay đổi key thường xuyên. Các  bên giao tiếp sẽ phải chia sẻ key để có thể giải - mã hoá dữ liệu thông qua việc  trao đổi trực tiếp hoặc gián tiếp qua một nền tảng trung gian; ngoài ra, key cần  được thay đổi thường xuyên để những kẻ tấn công không thể tìm ra được. Thời  gian để kẻ tấn công tìm ra được key phụ thuộc vào độ phức tạp của key cùng  cách chia sẻ key, nhưng việc ‘tái chế’ lại hình thức chia sẻ và key lâu dần vô hình  chung sẽ hình thành cơ sở để bên tấn công tìm ra và giải mã được, từ đó chiếm  đoạt dữ liệu.
    
    Mã khóa công khai, còn được gọi là mật mã bất đối xứng, không yêu cầu phải  chia sẻ chung. Nó bảo mật dựa trên mối quan hệ toán học giữa nhiều key, một  key công khai và một key riêng tư, key công khai được mở cho tất cả mọi người.  Bất kỳ ai cũng có thể truy cập và mã hóa dữ liệu bằng nó. Tuy nhiên, sau khi được  mã hóa, dữ liệu đó chỉ có thể được mở bằng cách sử dụng key riêng tương ứng,  key riêng tư phải được giữ bí mật để giữ cho nó không bị xâm phạm. Chính vì vậy,  chỉ khi người được ủy quyền, máy chủ, máy móc hoặc công cụ mới có quyền truy  cập vào key riêng tư. Khả năng độc đáo của mã khóa công khai gồm việc tạo và chia sẻ key bí mật cũng như cung cấp dịch vụ xác thực an toàn (secure  authentication) và chống chối bỏ an toàn (secure nonrepudiation), ngoài ra đó còn được gọi là hàm một chiều vì chúng tương đối dễ tính toán nhưng cực kỳ khó đảo ngược. Các hệ thống áp dụng mã hóa công khai có tính bảo mật cao và gần  như không thể xuyên thủng vì thế hạn chế được các cuộc tấn công mạng. Các  thuật toán phổ biến cho mã hóa bất đối xứng (asymmetric encryption) và trao đổi  khóa là Diffie-Hellman, RSA , ECDSA, ElGamal và DSA, loại hình này sử dụng các  khóa dài 1024 bit, 2048 bit hoặc hơn. Nhìn chung, kích thước khóa càng dài thì mã hóa càng an toàn. Nhưng vì tốc độ xử lý kinh khủng của máy tính lượng tử, cả việc mã hoá đối xứng và bất đối xứng đều đang đứng trước bờ vực sụp đổ.
    
    SSL (Secure Sockets Layer) hay lớp socket bảo mật, một loại bảo mật mã hoá liên lạc giữa website và trình duyệt, nó đã trở nên lỗi thời và được thay thế bởi TLS  (Transport Layer Security) vì SSL không còn được phát triển nữa, TLS có chức  năng tương tự như SSL chỉ khác tên gọi. Loại hình này bảo mật các thông tin dữ liệu trong quá trình truyền tải internet như số an sinh xã hội, thông tin giao dịch  ngân hàng, tài khoản mạng xã hội, vân vân. Giao thức SSL/TLS cho phép khách  truy cập truyền tải thông tin lên web server an toàn và bảo mật, đảm bảo mọi dữ liệu lúc di chuyển không bị xâm nhập hay tấn công bởi bên thứ ba. Nó hoạt động  dựa trên cách key công khai và key riêng tư cùng các key duy nhất của mỗi phiên  truyền tải. Với bảo mật internet, mỗi khi khách truy cập điền vào thanh địa chỉ SSL  thông tin web browser hoặc chuyển hướng tới trang web được bảo mật, trình  duyệt và web server đã thiết lập kết nối. Mã hoá email (tiện ích mở rộng thư internet an toàn/đa năng hay S/MIME) được sử dụng bên cạnh các liên lạc an  toàn do SSL/TLS cung cấp để tăng cường bảo vệ thông tin liên lạc của người  dùng. VPN và mạng nội bộ, việc để nhân viên và đối tác đáng tin cậy có quyền  truy cập từ xa vào tài nguyên thông tin của tổ chức là điều khá phổ biến. Điều này  thường yêu cầu VPN tạo ra một đường hầm liên lạc an toàn xuyên qua lớp bảo  mật ranh giới của tổ chức để cho phép truy cập vào thông tin và tài nguyên nội bộ và SSL/TLS được sử dụng để bảo vệ thông tin xác thực truy cập khỏi bị thu thập  trong khi truyền. Hay trong internet vạn vật (Internet of Things - IoT), SSL/TLS vẫn  đóng một vai trò quan trọng trong việc đảm bảo rằng các thông tin liên lạc này  được truyền bên trong một đường hầm an toàn trên mạng công cộng. 
    
    Có vẻ SSL/TLS là hình thức bảo mật an toàn và đa năng, nhưng trong kỉ nguyên  của công nghệ lượng tử cùng với sự phát triển như vũ bão của máy tính lượng tử,  giao thức SSL/TLS đang bị đe doạ. Đầu tiên là mối đe dọa đến từ nội bộ, hình  thức hữu ích nhất hiện có để bảo vệ chống lại các mối đe dọa nội bộ là kiểm soát  quyền truy cập và các hình thức mã hóa; các tổ chức sẽ rất khó tự bảo vệ bản  thân nếu bên tấn công sử dụng máy tính lượng tử để khai thác mật mã key công  khai như mã được tìm thấy trong TLS/SSL để truy cập vào mạng, email bảo mật  và tài liệu được mã hóa. Thứ hai, các quy trình kiểm soát truy cập mạnh mẽ (strong access control processes) ngăn chặn cuộc tấn công từ bên ngoài bằng  việc xử lý mật khẩu bằng kỹ thuật băm (hashing method), nhưng với máy tính  lượng tử, nó sẽ khai thác vào các đường hầm SSL/TLS từ đó lấy được những  thông tin xác thực trong quá trình truyền tải dữ liệu; đối với các chương trình bảo  mật phức tạp hơn, máy tính lượng tử sẽ giúp bên tác nhân đe doạ giả mạo danh  tính kỹ thuật số (digital identity) của người dùng bất kỳ, tức là tự tạo ra một key  riêng cho danh tính giả mạo đó; tương tự vậy kẻ tấn công có khả năng giả mạo  được danh tính của cả những máy chủ web. Thứ ba, che dấu đi dấu hiệu bị tấn  công, tác nhân tấn công chỉ cần truy cập vào dữ liệu được mã hóa. Họ có thể thu  thập nó khi nó truyền qua Internet, lấy nó từ đường truyền tạo riêng hoặc nguồn  cung cấp dữ liệu vệ tinh, hoặc thậm chí là hối lộ, ép buộc người trong nội bộ lấy  nó từ mạng và cơ sở dữ liệu nội bộ. Sau khi có được dữ liệu, tác nhân tấn công có thể xử lý dữ liệu đó bất cứ khi nào có sẵn tài nguyên điện toán lượng tử. Thứ tư,  các cuộc tấn công lượng tử sẽ không xảy ra trong thời gian thực. Các tác nhân  tấn công sẽ thu thập dữ liệu, là việc có thể xảy ra bất kỳ lúc nào, và lưu trữ dữ liệu  đó để xử lý ngoại tuyến khi thời gian trên máy tính lượng tử có hiệu lực. Hoặc kẻ tấn công có thể sắp xếp sàng lọc dữ liệu được mã hóa trực tiếp từ vị trí lưu trữ dự phòng của tổ chức. Tác nhân đe dọa duy nhất có thể tiếp cận quá trình xử lý
    lượng tử dữ liệu lớn hoặc gần thời gian thực sẽ là các quốc gia có quyền truy cập  sớm và kiểm soát các tài nguyên lượng tử chuyên dụng. Thứ năm, hãy hình dung  rằng bạn có một ổ khoá Việt Tiệp cùi ngô, theo lẽ thường sẽ không một ai phá cái  
    ổ đấy làm gì bởi nó quá cùi; nhưng tự nhiên một khứa nào đấy vác kìm cộng lực  tới rồi cắt nó cái một, tại sao khứa đấy lại làm vậy? Hẳn là do thứ bên trong được  chiếc ổ khoá cùi đấy bảo vệ có giá trị và nó thật sự đáng để làm vậy. Quay lại vấn  đề, các tác nhân tấn công thường tìm kiếm những mẩu dữ liệu có giá trị cao, hữu  dụng lâu dài có ổ khoá tương đối nhỏ để dễ xâm nhập. Nếu quy trình liên quan  đến việc đặt các key trên mạng tại bất kỳ thời điểm nào trong quá trình truyền tải  giữa các pháo đài kỹ thuật số an toàn (secure digital fortresses), thì máy tính  lượng tử có thể thu thập, lọc và giải mã dữ liệu chứa các key chính đó và bất kỳ thông tin hoặc hoạt động nào được bảo vệ bởi các key chính này về sau sẽ trở nên dễ bị tấn công. 
    """)

    st.markdown("<h2 style='color: #51C95D;'>3. Mặt tích cực cùng những ứng dụng của máy tính lượng tử. </h2>", unsafe_allow_html=True)
    st.image("./assets/images/ggmeme.jpg", width=850, channels="RGB")

    st.write("""
    Sau những ví dụ vừa rồi, chắc các bạn sẽ tưởng tượng Máy tính Lượng tử như là một cái gì đó mang lại diệt vong cho văn minh nhân loại, nhưng không thật sự là như vậy. Bây giờ chúng ta sẽ điểm qua mặt tích cực của công cụ thần kì này. 
    
    Trước hết, hãy tưởng tượng Google và IBM đang tổ chức một buổi trình diễn thời  trang điện toán lượng tử. Nó giống như một cuộc showdown công nghệ, nhưng  thay vì súng lục vào lúc bình minh, họ sử dụng qubit và thuật toán. Bây giờ, hãy  nói về những ngôi sao thực sự của chương trình: các ứng dụng của điện toán  lượng tử. 
    
    Bạn có biết những tiện ích thông minh có thể nhận dạng khuôn mặt của bạn và hiểu những gì bạn đang nói không? Điện toán lượng tử đưa điều đó lên một tầm 
    cao mới. Nó giống như việc đưa cho AI một con Turbo Boost, khiến nó thông  minh hơn và nhanh hơn bao giờ hết. 
    
    Hơn nữa, hóa học lượng tử có thể giúp tạo ra các loại thuốc tốt hơn, loại bỏ carbon dioxide trong không khí và thậm chí tạo ra pin không phát nổ. Việc tạo ra  các loại thuốc mới từng giống như ném mì spaghetti vào tường và xem liệu nó có dính vào không. Nhưng với điện toán lượng tử, tất cả mọi thứ đều có thể. Chúng  ta đang nói về việc tiết kiệm tiền bạc, thời gian và thậm chí có thể khám phá ra  cách chữa trị cảm lạnh thông thường. 
    
    Hãy tưởng tượng một pháo đài ảo được bảo vệ bởi các thuật toán lượng tử, đó là tương lai của bảo mật trực tuyến khi mà bạn sẽ không còn lo lắng về việc tin tặc  đánh cắp video về mèo của bạn. 
    """)

    st.markdown("<h2 style='color: #51C95D;'>4. Thành tựu đã đạt được đến hiện nay của Máy tính lượng tử. </h2>", unsafe_allow_html=True)
    st.write("""
    Sau khi tìm hiểu xong về lợi ích của điện toán lượng tử, điều quan trọng bây giờ là tìm hiểu những thay đổi mang tính đột phá và những lợi ích sâu sắc mà chúng  mang lại. 
    """)
    st.image("https://static01.nyt.com/images/2019/11/01/opinion/30Aaronson1/30Aaronson1-videoSixteenByNineJumbo1600.png", width=850, channels="RGB", caption="Vào tháng 10 năm 2019, Google xác nhận rằng họ đã đạt được ưu thế lượng  tử bằng cách sử dụng bộ xử lý 54 qubit có thể lập trình hoàn toàn có tên  Sycamore. ")

    st.write("""
    Trong y tế, vào năm 2022, con người ta cũng bắt đầu thấy những lợi ích  không tưởng mà điện toán lượng tử có thể mang lại. Trong một thế giới nơi  máy tính lượng tử kết hợp với AI, giải trình tự DNA và Big Data, các công  nghệ mô phỏng công nghệ cao tinh vi cùng nhau lập liên minh, tạo ra một  phòng thí nghiệm công nghệ đến cả Tony Stark cũng phải ganh tị.
    """)

    st.markdown("<h2 style='color: #51C95D;'>5. Vì sao Máy tính Lượng tử chưa được sử dụng rộng rãi ?. </h2>",unsafe_allow_html=True)
    st.write("""
    Một từ thôi: Đó là vì decoherence (tạm dịch là sự mất mạch lạc).
    Các bạn có thể hiểu rằng việc cố gắng chế tạo một máy tính lượng tử giống như cố gắng giữ yên một đứa trẻ hiếu động. Bạn sẽ có những hệ lượng tử đơn lẻ, ví dụ như các nguyên tử hay photon đầy nổi loạn, không thể cưỡng nổi việc hòa trộn với  môi trường xung quanh. Bữa tiệc tất niên chúng dự vui nhộn và thú vị cho đến khi  decoherence xuất hiện và đánh cắp toàn bộ lượng tử. 
        """)

    st.markdown("<h2 style='color: #51C95D;'>6. Kết luận  </h2>",unsafe_allow_html=True)
    st.write("""
    Tốc độ xử lý phi thường của máy tính lượng tử có thể tác động tiêu cực hoặc tích  cực đến bảo mật thông tin, hiện hữu những mối lo ngại trong các tổ chức và trong cộng đồng chuyên gia an ninh mạng về việc máy tính lượng tử sẽ phá hủy  thuật toán mã hóa hiện tại như thế nào. Nhưng nếu xem xét dưới một góc nhìn  khách quan, máy tính lượng tử không quá tệ từ góc độ bảo mật như chúng được  miêu tả hiện nay; những lợi ích mà máy tính lượng tử mang lại có thể cao hơn mối  nguy hiểm mà chúng gây ra. Giống như một đứa bạn thiên tài - có khả năng giải  quyết những vấn đề khó hiểu trong chớp mắt, nhưng cũng có khả năng vô tình  đốt cháy ngôi nhà của bạn khi cố gắng pha một tách cà phê hoàn hảo. Hiện tại,  chúng có khả năng phá vỡ tất cả những gì chúng ta biết về những thứ hiện tại,  nhưng có khi chính một chút sự hỗn loạn ấy lại đem đến cho ta những bước đột  phá công nghệ trong tương lai. 
    """)
with tab2:
    st.write("# *Không có Demo cho bài này*")

with tab3:
    # Create two columns with a ratio of 1:2
    col1, col2 = st.columns([1, 2])

    # In the first column, display the image
    with col1:
        pass

    # In the second column, display the heading
    with col2:
        st.image("./assets/images/F-Code_logo.png", width=280)
        st.markdown("<h2 style='color: #FFC81B;'>Nguồn Tham Khảo</h2>", unsafe_allow_html=True)
    st.write("")
    st.write("""
           - 1. J. Mulholland, M. Mosca and J. Braun, "The Day the Cryptography Dies," in IEEE  Security & Privacy, vol. 15, no. 4, pp. 14-21, 2017, doi: 10.1109/MSP.2017.3151325. 
            
           - 2. M. Njorbuenwu, B. Swar and P. Zavarsky, "A Survey on the Impacts of Quantum  Computers on Information Security," 2019 2nd International Conference on Data  Intelligence and Security (ICDIS), South Padre Island, TX, USA, 2019, pp. 212-218, doi:  10.1109/ICDIS.2019.00039.
            """)
