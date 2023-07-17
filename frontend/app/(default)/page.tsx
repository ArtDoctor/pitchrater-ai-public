export const metadata = {
  title: 'Home',
}

import Hero from '@/components/hero'
import Features from '@/components/features'
import Zigzag from '@/components/zigzag'
import Footer from '@/components/ui/footer'
import ModalVideo from '@/components/modal-video'

export default function Home() {
  return (
    <>
      <Hero />
      <Features />
    </>
  )
}
