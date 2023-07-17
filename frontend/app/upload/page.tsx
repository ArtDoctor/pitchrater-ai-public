import Uploader from './uploader';
import Footer from '@/components/ui/footer'

export const metadata = {
  title: 'Upload Pitch',
}

export default function UploadPage() {
  return (
    <>
      <Uploader/>
      <Footer />
    </>
  )
}
